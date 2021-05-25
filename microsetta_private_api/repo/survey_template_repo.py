from werkzeug.exceptions import NotFound

from microsetta_private_api import localization
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.survey_template import SurveyTemplate, \
    SurveyTemplateLinkInfo
from microsetta_private_api.model.survey_template_group import \
        SurveyTemplateGroup
from microsetta_private_api.model.survey_template_question import \
        SurveyTemplateQuestion
from microsetta_private_api.model.survey_template_trigger import \
        SurveyTemplateTrigger
import copy
import secrets

from microsetta_private_api.repo.sample_repo import SampleRepo


class SurveyTemplateRepo(BaseRepo):

    VIOSCREEN_ID = 10001
    SURVEY_INFO = {
        1: SurveyTemplateLinkInfo(
            1,
            "Primary",
            "1.0",
            "local"
        ),
        2: SurveyTemplateLinkInfo(
            2,
            "Pet Information",
            "1.0",
            "local"
        ),
        3: SurveyTemplateLinkInfo(
            3,
            "Fermented Foods Questionnaire",
            "1.0",
            "local"
        ),
        4: SurveyTemplateLinkInfo(
            4,
            "Surfer Questionnaire",
            "1.0",
            "local"
        ),
        5: SurveyTemplateLinkInfo(
            5,
            "Personal Microbiome Information",
            "1.0",
            "local"
        ),
        6: SurveyTemplateLinkInfo(
            6,
            "COVID-19 Questionnaire",
            "1.0",
            "local"
        ),
        VIOSCREEN_ID: SurveyTemplateLinkInfo(
            VIOSCREEN_ID,
            "Vioscreen Food Frequency Questionnaire",
            "1.0",
            "remote"
        )
    }

    def __init__(self, transaction):
        super().__init__(transaction)

    def list_survey_ids(self):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT DISTINCT survey_id from surveys")
            rows = cur.fetchall()
        return [x[0] for x in rows]

    @staticmethod
    def get_survey_template_link_info(survey_id):
        return copy.deepcopy(SurveyTemplateRepo.SURVEY_INFO[survey_id])

    def get_survey_template(self, survey_id, language_tag):
        tag_to_col = {
            localization.EN_US: "survey_question.american",
            localization.EN_GB: "survey_question.british",
            localization.ES_MX: "survey_question.spanish"
        }

        if language_tag not in tag_to_col:
            raise NotFound("Survey localization unavailable: %s" %
                           language_tag)

        with self._transaction.cursor() as cur:

            cur.execute(
                "SELECT count(*) FROM surveys WHERE survey_id=%s",
                (survey_id,)
            )
            if cur.fetchone()[0] == 0:
                raise NotFound("No such survey")

            cur.execute(
                "SELECT "
                "group_questions.survey_group, "
                "survey_question.survey_question_id, " +
                tag_to_col[language_tag] + ", " +
                "survey_question.question_shortname, "
                "survey_question_response_type.survey_response_type "
                "FROM "
                "surveys "
                "LEFT JOIN group_questions ON "
                "surveys.survey_group = group_questions.survey_group "
                "LEFT JOIN survey_question ON "
                "group_questions.survey_question_id = "
                "survey_question.survey_question_id "
                "LEFT JOIN survey_question_response_type ON "
                "survey_question.survey_question_id = "
                "survey_question_response_type.survey_question_id "
                "WHERE surveys.survey_id = %s AND "
                "survey_question.retired = false "
                "ORDER BY group_questions.survey_group, "
                "group_questions.display_index",
                (survey_id,))

            rows = cur.fetchall()

            all_groups = []
            cur_group_id = None
            cur_questions = None

            for r in rows:
                group_id = r[0]
                question_id = r[1]
                localized_text = r[2]
                short_name = r[3]
                response_type = r[4]
                if group_id != cur_group_id:
                    if cur_group_id is not None:
                        group_localized_text = self._get_group_localized_text(
                                                                cur_group_id,
                                                                language_tag)
                        all_groups.append(SurveyTemplateGroup(
                            group_localized_text,
                            cur_questions))
                    cur_group_id = group_id
                    cur_questions = []

                responses = self._get_question_valid_responses(question_id,
                                                               language_tag)
                triggers = self._get_question_triggers(question_id)

                question = SurveyTemplateQuestion(question_id,
                                                  localized_text,
                                                  short_name,
                                                  response_type,
                                                  responses,
                                                  triggers)
                cur_questions.append(question)

            if cur_group_id is not None:
                group_localized_text = self._get_group_localized_text(
                    cur_group_id,
                    language_tag)
                all_groups.append(SurveyTemplateGroup(
                    group_localized_text,
                    cur_questions))

            return SurveyTemplate(survey_id, language_tag, all_groups)

    def _get_group_localized_text(self, group_id, language_tag):
        tag_to_col = {
            localization.EN_US: "american",
            localization.EN_GB: "british",
            localization.ES_MX: "american"
        }
        with self._transaction.cursor() as cur:
            cur.execute("SELECT " +
                        tag_to_col[language_tag] + " " +
                        "FROM survey_group "
                        "WHERE "
                        "group_order = %s", (group_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]

    def _get_question_valid_responses(self, survey_question_id, language_tag):
        tag_to_col = {
            localization.EN_US: "survey_question_response.american",
            localization.EN_GB: "survey_question_response.british",
            localization.ES_MX: "survey_question_response.spanish",
        }

        with self._transaction.cursor() as cur:
            cur.execute("SELECT " +
                        tag_to_col[language_tag] + " "
                        "FROM "
                        "survey_question_response "
                        "LEFT JOIN "
                        "survey_response "
                        "ON "
                        "survey_question_response.response = "
                        "survey_response.american "
                        "WHERE "
                        "survey_question_id = %s "
                        "ORDER BY "
                        "display_index", (survey_question_id,))
            return [x[0] for x in cur.fetchall()]

    def _get_question_triggers(self, survey_question_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT triggering_response, triggered_question "
                        "FROM "
                        "survey_question_triggers "
                        "WHERE "
                        "survey_question_id = %s ", (survey_question_id,))

            rows = cur.fetchall()
            return [SurveyTemplateTrigger(x[0], x[1]) for x in rows]

    def create_vioscreen_id(self, account_id, source_id,
                            vioscreen_ext_sample_id):
        with self._transaction.cursor() as cur:
            # test if an existing ID is available
            existing = self.get_vioscreen_id_if_exists(account_id, source_id,
                                                       vioscreen_ext_sample_id)
            if existing is None:
                vioscreen_id = secrets.token_hex(8)
                # Put a survey with status -1 into ag_login_surveys
                cur.execute("INSERT INTO ag_login_surveys("
                            "ag_login_id, "
                            "survey_id, "
                            "vioscreen_status, "
                            "source_id) "
                            "VALUES(%s, %s, %s, %s)",
                            (account_id, vioscreen_id, -1, source_id))
                # Immediately attach that survey to the specified sample
                sample_repo = SampleRepo(self._transaction)
                s = sample_repo.get_sample(account_id,
                                           source_id,
                                           vioscreen_ext_sample_id)

                if s is None:
                    raise KeyError(f"{vioscreen_ext_sample_id} does not exist")

                cur.execute("INSERT INTO source_barcodes_surveys "
                            "(barcode, survey_id) "
                            "VALUES(%s, %s)", (s.barcode, vioscreen_id))

                # And add it to the registry to keep track of the survey if
                # user quits out then wants to resume the survey.
                cur.execute("INSERT INTO vioscreen_registry("
                            "account_id, source_id, sample_id, vio_id) "
                            "VALUES(%s, %s, %s, %s)",
                            (account_id, source_id, vioscreen_ext_sample_id,
                             vioscreen_id))
            else:
                vioscreen_id = existing
        return vioscreen_id

    def get_vioscreen_id_if_exists(self, account_id, source_id,
                                   vioscreen_ext_sample_id):
        """Obtain a vioscreen ID if it exists"""
        with self._transaction.cursor() as cur:
            # Find an active vioscreen survey for this account+source+sample
            # (deleted surveys are not active)
            cur.execute("SELECT vio_id FROM vioscreen_registry WHERE "
                        "account_id=%s AND "
                        "source_id=%s AND "
                        "sample_id=%s AND "
                        "deleted=false",
                        (account_id, source_id, vioscreen_ext_sample_id))
            rows = cur.fetchall()
            if rows is None or len(rows) == 0:
                return None
            else:
                return rows[0][0]

    def fetch_user_birth_year_gender(self, account_id, source_id):
        """Given an account ID,
        returns a tuple of (birth_year->int|None and gender->str|None)"""
        birth_year = None
        gender = None
        with self._transaction.cursor() as cur:
            # question IDs: 107 = gender, 112 = birth year
            cur.execute("""SELECT q.survey_question_id, q.response
                           FROM ag_login_surveys AS s
                           JOIN survey_answers AS q
                             ON s.survey_id = q.survey_id
                           WHERE survey_question_id IN (112, 107)
                             AND s.ag_login_id = %s
                             and s.source_id = %s""",
                        (account_id, source_id))
            for row in cur:
                if row[0] == 107:
                    gender = row[1]
                    if gender == 'Unspecified':
                        gender = None
                elif row[0] == 112:
                    try:
                        birth_year = int(row[1])
                    except ValueError:
                        pass  # for 'Unspecified', stays None
        return (birth_year, gender)
