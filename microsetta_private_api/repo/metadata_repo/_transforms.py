from ._constants import MISSING_VALUE
from functools import reduce
from operator import or_
import pandas as pd
import numpy as np


WEIGHT_KG = 'weight_kg'
WEIGHT_UNITS = 'weight_units'
HEIGHT_CM = 'height_cm'
HEIGHT_UNITS = 'height_units'
BIRTH_YEAR = 'birth_year'
BIRTH_MONTH = 'birth_month'
COLLECTION_TIMESTAMP = 'collection_timestamp'
BMI_ = 'bmi'
AGE_YEARS = 'age_years'
AGE_CAT = 'age_cat'
BMI_CAT = 'bmi_cat'
INCHES = 'inches'
CENTIMETERS = 'centimeters'
POUNDS = 'pounds'
KILOGRAMS = 'kilograms'
ALCOHOL_CONSUMPTION = 'alcohol_consumption'
ALCOHOL_FREQUENCY = 'alcohol_frequency'
SEX = 'sex'
GENDER = 'gender'


class Transformer:
    REQUIRED_COLUMNS = None
    COLUMN_NAME = None
    EXISTING_UNITS_COL_UPDATE = None

    @classmethod
    def satisfies_requirements(cls, df):
        return cls.REQUIRED_COLUMNS.issubset(set(df.columns))

    @classmethod
    def apply(cls, df):
        return cls._transform(df).fillna(MISSING_VALUE)

    @classmethod
    def _transform(cls, df):
        raise NotImplementedError

    @staticmethod
    def not_null_map(*args):
        # args are expected to be pd.Series instances

        # reduce(or_, ...) acts as an elementwise logical OR

        # ~(...) performs an elementwise logical NOT
        return ~(reduce(or_, map(pd.isnull, args)))

    @classmethod
    def basis(cls, index):
        return pd.Series([None] * len(index), index=index,
                         name=cls.COLUMN_NAME)


class BMI(Transformer):
    REQUIRED_COLUMNS = frozenset([WEIGHT_KG, HEIGHT_CM])
    COLUMN_NAME = BMI_

    @classmethod
    def _transform(cls, df):
        # weight in kilograms / (height in meters)^2
        weight = pd.to_numeric(df[WEIGHT_KG], errors='coerce')
        height = pd.to_numeric(df[HEIGHT_CM], errors='coerce')
        height /= 100  # covert to meters
        height *= height  #

        not_null_map = cls.not_null_map(weight, height)

        series = cls.basis(df.index)
        series.loc[not_null_map] = \
            (weight.loc[not_null_map] / height.loc[not_null_map]).round(1)

        return series


class AgeYears(Transformer):
    REQUIRED_COLUMNS = frozenset([BIRTH_YEAR, BIRTH_MONTH,
                                  COLLECTION_TIMESTAMP])
    COLUMN_NAME = AGE_YEARS

    @classmethod
    def _transform(cls, df):
        def make_month_year(row):
            # TODO: this function can probably be greatly reduced
            # if only applied to positions which assessed to be not null
            # prior
            mo = row[BIRTH_MONTH]
            yr = row[BIRTH_YEAR]
            if pd.isnull(mo) or pd.isnull(yr):
                return '-'
            else:
                return '%s-%s' % (mo, yr)

        birth_month_year = df.apply(make_month_year, axis=1)
        birth_month_year = pd.to_datetime(birth_month_year, errors='coerce',
                                          format='%B-%Y')
        collection_timestamp = pd.to_datetime(df[COLLECTION_TIMESTAMP],
                                              errors='coerce')

        not_null_map = cls.not_null_map(birth_month_year, collection_timestamp)

        series = cls.basis(df.index)

        collection_timestamp = collection_timestamp[not_null_map]
        birth_month_year = birth_month_year[not_null_map]

        # compute timedelta64 types, and express as year
        td = collection_timestamp - birth_month_year
        td_as_year = (td / np.timedelta64(1, 'Y')).round(1)
        series.loc[not_null_map] = td_as_year

        return series


class AgeCat(Transformer):
    REQUIRED_COLUMNS = frozenset([AGE_YEARS, ])
    COLUMN_NAME = AGE_CAT

    @classmethod
    def _transform(cls, df):
        # these bounds are based on the values previously used for metadata
        # pulldown in labadmin
        bounds = [('baby', 0, 3),
                  ('child', 3, 13),
                  ('teen', 13, 20),
                  ('20s', 20, 30),
                  ('30s', 30, 40),
                  ('40s', 40, 50),
                  ('50s', 50, 60),
                  ('60s', 60, 70),
                  ('70+', 70, 123)]

        age_years = pd.to_numeric(df[AGE_YEARS], errors='coerce')
        age_cat = cls.basis(df.index)

        for label, lower, upper in bounds:
            # this bounds checking is consistent with that used for metadata
            # pulldown in labadmin where the lowerbound is inclusive and
            # upperbound is exclusive.
            positions = (age_years >= lower) & (age_years < upper)
            age_cat.loc[positions] = label

        return age_cat


class BMICat(Transformer):
    REQUIRED_COLUMNS = frozenset([BMI, ])
    COLUMN_NAME = BMI_CAT

    @classmethod
    def _transform(cls, df):
        # these bounds are based on the values previously used for metadata
        # pulldown in labadmin
        bounds = [('Underweight', 8, 18.5),
                  ('Normal', 18.5, 25),
                  ('Overweight', 25, 30),
                  ('Obese', 30, 80)]
        bmi = pd.to_numeric(df[BMI_], errors='coerce')
        bmi_cat = cls.basis(df.index)

        for label, lower, upper in bounds:
            # this bounds checking is consistent with that used for metadata
            # pulldown in labadmin where the lowerbound is inclusive and
            # upperbound is exclusive.
            positions = (bmi >= lower) & (bmi < upper)
            bmi_cat.loc[positions] = label

        return bmi_cat


class AlcoholConsumption(Transformer):
    REQUIRED_COLUMNS = frozenset([ALCOHOL_FREQUENCY, ])
    COLUMN_NAME = ALCOHOL_CONSUMPTION

    @classmethod
    def _transform(cls, df):
        mapping = {'Rarely (a few times/month)': 'Yes',
                   'Occasionally (1-2 times/week)': 'Yes',
                   'Regularly (3-5 times/week)': 'Yes',
                   'Daily': 'Yes',
                   'Never': 'No',
                   'Unspecified': MISSING_VALUE,
                   MISSING_VALUE: MISSING_VALUE}

        # using value_counts() here as it drops NA by default whereas
        # unique() retains NA values.
        observed_values = set(df[ALCOHOL_FREQUENCY].value_counts().index)
        if not observed_values.issubset(mapping):
            raise KeyError("Unexpected values present in column %s: %s" %
                           (ALCOHOL_FREQUENCY, observed_values - set(mapping)))

        series = df[ALCOHOL_FREQUENCY].replace(mapping, inplace=False)
        series.name = cls.COLUMN_NAME
        return series


class Sex(Transformer):
    # The existing pulldown code cast entries of GENDER to lowercase, and
    # stored them within the SEX variable. Adding here for consistency
    # with existing metadata in Qiita.
    REQUIRED_COLUMNS = frozenset([GENDER, ])
    COLUMN_NAME = SEX

    @classmethod
    def _transform(cls, df):
        mapping = {'Female': 'female',
                   'Male': 'male',
                   'Other': 'other',

                   # Lower case is not ideal here, however that's what is
                   # presently in Qiita
                   'Unspecified': 'unspecified',
                   MISSING_VALUE: MISSING_VALUE}

        observed_values = set(df[GENDER].value_counts().index)
        if not observed_values.issubset(mapping):
            raise KeyError("Unexpected values present in column %s: %s" %
                           (GENDER, observed_values - set(mapping)))

        series = df[GENDER].replace(mapping, inplace=False)
        series.name = cls.COLUMN_NAME
        return series


def _normalizer(df, focus_col, units_col, units_value, factor):
    # get our columns
    focus = pd.to_numeric(df[focus_col], errors='coerce')
    units = df[units_col]

    # operate on a copy as to retain non-unit focus values (e.g., values
    # already expressed as centimeters
    result = focus.copy()

    # anything negative is weird so kill it
    result[result < 0] = None

    # figure out what positions are safe to operate on
    not_null_map = Transformer.not_null_map(result, units)

    # take entries like where either focus or units are null and kill them
    result.loc[not_null_map[~not_null_map].index] = None

    # reduce to only those safe to operate on
    focus_not_null = result[not_null_map]
    units_not_null = units[not_null_map]
    focus_adj = focus_not_null.loc[units_not_null == units_value]

    # adjust the indices that need adjustment
    result.loc[focus_adj.index] = focus_adj * factor

    return result


class _Normalize(Transformer):
    FOCUS_COL = None
    FOCUS_UNITS = None
    UNITS_COL = None
    FACTOR = None

    @classmethod
    def _transform(cls, df):
        return _normalizer(df, cls.FOCUS_COL, cls.UNITS_COL, cls.FOCUS_UNITS,
                           cls.FACTOR)


class NormalizeHeight(_Normalize):
    REQUIRED_COLUMNS = frozenset([HEIGHT_UNITS, HEIGHT_CM])
    COLUMN_NAME = HEIGHT_CM

    # after normalization to centimeters, we need to also update the
    # height_units column to reflect these values are now centimeters
    EXISTING_UNITS_COL_UPDATE = (HEIGHT_UNITS, CENTIMETERS)
    FOCUS_COL = HEIGHT_CM
    UNITS_COL = HEIGHT_UNITS
    FOCUS_UNITS = INCHES
    FACTOR = 2.54


class NormalizeWeight(_Normalize):
    REQUIRED_COLUMNS = frozenset([WEIGHT_UNITS, WEIGHT_KG])
    COLUMN_NAME = WEIGHT_KG

    # after normalization to kilograms, we need to also update the
    # weight_units column to reflect these values are now in kg
    EXISTING_UNITS_COL_UPDATE = (WEIGHT_UNITS, KILOGRAMS)
    FOCUS_COL = WEIGHT_KG
    FOCUS_UNITS = POUNDS
    UNITS_COL = WEIGHT_UNITS
    FACTOR = (1 / 2.20462)


# transforms are order dependent as some entries (e.g., BMICat) depend
# on the presence of a BMI column
HUMAN_TRANSFORMS = (AgeYears, AgeCat, NormalizeWeight, NormalizeHeight,
                    BMI, BMICat, AlcoholConsumption, Sex)


def apply_transforms(df, transforms):
    for transform in transforms:
        if transform.satisfies_requirements(df):
            # note: not using df.apply here as casts are needed on a
            # case-by-case basis, and pandas is much more efficient
            # casting whole columns
            subset = df[transform.REQUIRED_COLUMNS]
            series = transform.apply(subset)

            # it is almost certainly the case that the input dataframe is
            # str already, so let's fall back. And these will be serialized
            # anyway w/o type information.
            series = series.astype(str)

            # NOTE: this operation can either change AN EXISTING column in the
            # DataFrame or ADD a column. Both are valid. Operations such as
            # the creation of "age_years" will CREATE a new column, whereas
            # the normalization of "height_cm" will MODIFY an existing one.
            df[transform.COLUMN_NAME] = series

            # update a an existing column if the transform needs to. An example
            # is with height, where once values are normalized to centimeters
            # within the height_cm column, we need to then also modify the
            # height_units column for all non-null height_cm entries as they
            # are assured to be centimeters.
            if transform.EXISTING_UNITS_COL_UPDATE is not None:
                column, value = transform.EXISTING_UNITS_COL_UPDATE
                df.loc[~df[transform.COLUMN_NAME].isnull(), column] = value

    return df
