-- add in translations for the covid questionnaire

UPDATE ag.survey_question SET "spanish" = '¿Cuál es su ocupación?' WHERE survey_question_id = '209';
UPDATE ag.survey_question SET "spanish" = 'Por favor, piense en su nivel actual de bienestar. Cuando pienses en el bienestar, piensa en tu salud física, en tu salud emocional, en cualquier desafío que estés experimentando, en las personas de tu vida y en las oportunidades o recursos que tienes a tu disposición. ¿Cómo describirías tu nivel actual de bienestar?' WHERE survey_question_id = '210';
UPDATE ag.survey_response SET "spanish" = 'No especificado' WHERE american = 'Unspecified';
UPDATE ag.survey_response SET "spanish" = 'Excelente' WHERE american = 'Excellent';
UPDATE ag.survey_response SET "spanish" = 'Muy bueno' WHERE american = 'Very good';
UPDATE ag.survey_response SET "spanish" = 'Bueno' WHERE american = 'Good';
UPDATE ag.survey_response SET "spanish" = 'Bajo' WHERE american = 'Fair';
UPDATE ag.survey_response SET "spanish" = 'Pobre' WHERE american = 'Poor';
UPDATE ag.survey_response SET "spanish" = 'Muy pobre' WHERE american = 'Very poor';

UPDATE ag.survey_question SET "spanish" = '¿Ha estado expuesto a alguien que puede tener Coronavirus/COVID-19? (marque todas las que correspondan)' WHERE survey_question_id = '211';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Sí, alguien con prueba positiva' WHERE american = 'Yes, someone with positive test';
UPDATE ag.survey_response SET "spanish" = 'Sí, alguien con diagnóstico médico, pero sin prueba' WHERE american = 'Yes, someone with medical diagnosis, but no test';
UPDATE ag.survey_response SET "spanish" = 'Sí, alguien con posibles síntomas, pero sin diagnóstico por parte del médico' WHERE american = 'Yes, someone with possible symptoms, but no diagnosis by doctor';
-- responses exists, 'No' -> 'No'

UPDATE ag.survey_question SET "spanish" = '¿Se ha sospechado que tiene infección por coronavirus/COVID-19?' WHERE survey_question_id = '212';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Sí,  con prueba positiva' WHERE american = 'Yes, with a positive test';
UPDATE ag.survey_response SET "spanish" = 'Sí,  con diagnóstico médico, pero sin prueba' WHERE american = 'Yes, medical diagnosis, but no test';
UPDATE ag.survey_response SET "spanish" = 'Sí,  con posibles síntomas, pero sin diagnóstico por parte del médico' WHERE american = 'Yes, have had some possible symptoms, but no diagnosis by doctor';
UPDATE ag.survey_response SET "spanish" = 'Sí, he tenido algunos posibles síntomas, pero di negativo' WHERE american = 'Yes, have had some possible symptoms but tested negative';
UPDATE ag.survey_response SET "spanish" = 'Sin síntomas ni signos' WHERE american = 'No symptoms or signs';

UPDATE ag.survey_question SET "spanish" = 'Proporcione la fecha' WHERE survey_question_id = '213';
UPDATE ag.survey_question SET "spanish" = 'Ha tenido alguno de los siguientes síntomas? (marque todas las que correspondan)' WHERE survey_question_id = '214';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Fiebre' WHERE american = 'Fever';
UPDATE ag.survey_response SET "spanish" = 'Tos' WHERE american = 'Cough';
UPDATE ag.survey_response SET "spanish" = 'Falta de respiración' WHERE american = 'Shortness of breath';
UPDATE ag.survey_response SET "spanish" = 'Dolor de garganta' WHERE american = 'Sore throat';
UPDATE ag.survey_response SET "spanish" = 'Fatiga' WHERE american = 'Fatigue';
UPDATE ag.survey_response SET "spanish" = 'Pérdida de sabor u olor' WHERE american = 'Loss of taste or smell';
UPDATE ag.survey_response SET "spanish" = 'Dolor en el pecho o opresión en el pecho' WHERE american = 'Chest pain or tightness in chest';
UPDATE ag.survey_response SET "spanish" = 'Diarrea' WHERE american = 'Diarrhea';
UPDATE ag.survey_response SET "spanish" = 'Nausea' WHERE american = 'Nausea';
UPDATE ag.survey_response SET "spanish" = 'Falta de apetito' WHERE american = 'Lack of appetitie';
UPDATE ag.survey_response SET "spanish" = 'Otro' WHERE american = 'Other';

UPDATE ag.survey_question SET "spanish" = NULL WHERE survey_question_id = '215';
UPDATE ag.survey_question SET "spanish" = 'En caso afirmativo a cualquier síntoma anterior, ¿se quedó en casa sin ir al trabajo mientras estaba sintomático?' WHERE survey_question_id = '216';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Si' WHERE american = 'Yes';
-- responses exists, 'No' -> 'No'

UPDATE ag.survey_question SET "spanish" = '¿Le ha pasado algo de lo siguiente a los miembros de su familia a causa del coronavirus/COVID-19? (marque todas las que correspondan)' WHERE survey_question_id = '217';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Se enfermo físicamente' WHERE american = 'Fallen ill physically';
UPDATE ag.survey_response SET "spanish" = 'Hospitalizado' WHERE american = 'Hospitalized';
UPDATE ag.survey_response SET "spanish" = 'Puesto en cuarentena con síntomas' WHERE american = 'Put into self-quarantine with symptoms';
UPDATE ag.survey_response SET "spanish" = 'Puesto en cuarentena sin síntomas (por ejemplo, debido a una posible exposición)' WHERE american = 'Put into self-quarantine without symptoms (e.g. due to possible exposure)';
UPDATE ag.survey_response SET "spanish" = 'Perdida de Trabajo' WHERE american = 'Lost job';
UPDATE ag.survey_response SET "spanish" = 'Reducción de la capacidad de ganar dinero' WHERE american = 'Reduced ability to earn money';
UPDATE ag.survey_response SET "spanish" = 'Muerte' WHERE american = 'Passed away';
UPDATE ag.survey_response SET "spanish" = 'Ninguno de los anteriores' WHERE american = 'None of the above';

UPDATE ag.survey_question SET "spanish" = '¿Cuántas veces ha salido de su casa por cualquier razón, incluido el trabajo (por ejemplo, ha dejado su propiedad para ir a tiendas, parques, etc.)?' WHERE survey_question_id = '218';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'No en absoluto' WHERE american = 'Not at all';
UPDATE ag.survey_response SET "spanish" = '1-2 días a la semana' WHERE american = '1-2 days per week';
UPDATE ag.survey_response SET "spanish" = 'Unos pocos días a la semana' WHERE american = 'A few days per week';
UPDATE ag.survey_response SET "spanish" = 'Varios días a la semana' WHERE american = 'Several days per week';
UPDATE ag.survey_response SET "spanish" = 'Todos los días' WHERE american = 'Every day';

UPDATE ag.survey_question SET "spanish" = 'Ha utilizado servicios de transporte compartidos como Lyft, Uber o formas alternativas de taxi?' WHERE survey_question_id = '219';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Yes' -> 'Si'
-- responses exists, 'No' -> 'No'

UPDATE ag.survey_question SET "spanish" = '¿Tiene alguna de las siguientes afecciones crónicas (marque todas las que correspondan):' WHERE survey_question_id = '220';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Alergias estacionales' WHERE american = 'Seasonal allergies';
UPDATE ag.survey_response SET "spanish" = 'Asma u otros problemas pulmonares' WHERE american = 'Asthma or other lung problems';
UPDATE ag.survey_response SET "spanish" = 'Problemas cardíacos' WHERE american = 'Heart problems';
UPDATE ag.survey_response SET "spanish" = 'Problemas renales' WHERE american = 'Kidney problems';
UPDATE ag.survey_response SET "spanish" = 'Trastorno inmune' WHERE american = 'Immune disorder';
UPDATE ag.survey_response SET "spanish" = 'Diabetes o nivel alto de azúcar en sangre' WHERE american = 'Diabetes or high blood sugar';
UPDATE ag.survey_response SET "spanish" = 'Cancer' WHERE american = 'Cancer';
UPDATE ag.survey_response SET "spanish" = 'Artritis' WHERE american = 'Arthritis';
UPDATE ag.survey_response SET "spanish" = 'Dolores de cabeza Frecuentes o muy fuertes' WHERE american = 'Frequent or very bad headaches';
UPDATE ag.survey_response SET "spanish" = 'Epilepsia o convulsiones' WHERE american = 'Epilepsy or seizures';
UPDATE ag.survey_response SET "spanish" = 'Problemas estomacales o intestinales graves' WHERE american = 'Serious stomach or bowel problems';
UPDATE ag.survey_response SET "spanish" = 'Acné grave o problemas de la piel' WHERE american = 'Serious acne or skin problems';
UPDATE ag.survey_response SET "spanish" = 'Hipertensión' WHERE american = 'Hypertension';
UPDATE ag.survey_response SET "spanish" = 'Enfermedad Pulmonar Obstructiva Crónica (EPOC)' WHERE american = 'Chronic Obstructive Pulmonary Disease (COPD)';
UPDATE ag.survey_response SET "spanish" = 'Falla cardiaca congestiva' WHERE american = 'Congestive Heart Failure';
UPDATE ag.survey_response SET "spanish" = 'Fibrilación o murmullo auriculares' WHERE american = 'Atrial Fibrillation or Atrial Flutter';
UPDATE ag.survey_response SET "spanish" = 'Enfermedad cardíaca / Infarto de miocardio' WHERE american = 'Heart disease / Myocardial infarction';
UPDATE ag.survey_response SET "spanish" = 'Derrame cerebral' WHERE american = 'Stroke';
UPDATE ag.survey_response SET "spanish" = 'Cualquier enfermedad autoinmune' WHERE american = 'Any autoimmune disease';
UPDATE ag.survey_response SET "spanish" = 'VIH' WHERE american = 'HIV';
UPDATE ag.survey_response SET "spanish" = 'Trombosis venosa profunda' WHERE american = 'Deep vein thrombosis';
UPDATE ag.survey_response SET "spanish" = 'Embolia pulmonar' WHERE american = 'Pulmonary embolism';

UPDATE ag.survey_question SET "spanish" = 'Durante las últimas 2 semanas, ¿con qué frecuencia te ha faltado interés o placer para hacer las cosas?' WHERE survey_question_id = '221';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Not at all' -> 'No en absoluto'
UPDATE ag.survey_response SET "spanish" = 'Uno o dos días' WHERE american = 'One or two days';
UPDATE ag.survey_response SET "spanish" = 'Varios días en la semana' WHERE american = 'Several days per week';
UPDATE ag.survey_response SET "spanish" = 'Más de la mitad de los días' WHERE american = 'More than half the days';
UPDATE ag.survey_response SET "spanish" = 'Casi todos los días' WHERE american = 'Nearly every day';

UPDATE ag.survey_question SET "spanish" = 'Durante las últimas 2 semanas, ¿con qué frecuencia se ha sentido deprimido o desesperanzado?' WHERE survey_question_id = '222';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Not at all' -> 'No en absoluto'
-- responses exists, 'One or two days' -> 'Uno o dos días'
-- responses exists, 'Several days per week' -> 'Varios días en la semana'
-- responses exists, 'More than half the days' -> 'Más de la mitad de los días'
-- responses exists, 'Nearly every day' -> 'Casi todos los días'

UPDATE ag.survey_question SET "spanish" = 'Durante las últimas 2 semanas, ¿con qué frecuencia se ha sentido ansioso o nervioso?' WHERE survey_question_id = '223';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Not at all' -> 'No en absoluto'
-- responses exists, 'One or two days' -> 'Uno o dos días'
-- responses exists, 'Several days per week' -> 'Varios días en la semana'
-- responses exists, 'More than half the days' -> 'Más de la mitad de los días'
-- responses exists, 'Nearly every day' -> 'Casi todos los días'

UPDATE ag.survey_question SET "spanish" = 'Durante las últimas 2 semanas, ¿con qué frecuencia no ha podido detener o controlar la preocupación?' WHERE survey_question_id = '224';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Not at all' -> 'No en absoluto'
-- responses exists, 'One or two days' -> 'Uno o dos días'
-- responses exists, 'Several days per week' -> 'Varios días en la semana'
-- responses exists, 'More than half the days' -> 'Más de la mitad de los días'
-- responses exists, 'Nearly every day' -> 'Casi todos los días'

UPDATE ag.survey_question SET "spanish" = '¿Está involucrado en la atención al paciente o trabaja en un entorno hospitalario / clínico?' WHERE survey_question_id = '225';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Yes' -> 'Si'
-- responses exists, 'No' -> 'No'

UPDATE ag.survey_question SET "spanish" = '¿ha participado en la atención directa al paciente en los últimos siete días?' WHERE survey_question_id = '226';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Yes' -> 'Si'
-- responses exists, 'No' -> 'No'
UPDATE ag.survey_response SET "spanish" = 'No aplica' WHERE american = 'Not applicable';

UPDATE ag.survey_question SET "spanish" = '¿ha participado en la atención directa al paciente que involucra a un paciente con COVID-19 confirmado en los últimos 7 días?' WHERE survey_question_id = '227';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Yes' -> 'Si'
-- responses exists, 'No' -> 'No'
-- responses exists, 'Not applicable' -> 'No aplica'

UPDATE ag.survey_question SET "spanish" = 'Durante cualquier interacción de atención médica con un paciente COVID-19, ¿con qué frecuencia pudo usar equipo protectivo según lo recomendado para el nivel de contacto?' WHERE survey_question_id = '228';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Siempre, como se recomienda' WHERE american = 'Always, as recommended';
UPDATE ag.survey_response SET "spanish" = 'La mayoría de las veces' WHERE american = 'Most of the time';
UPDATE ag.survey_response SET "spanish" = 'Ocasionalmente' WHERE american = 'Occasionally';
UPDATE ag.survey_response SET "spanish" = 'Rara vez' WHERE american = 'Rarely';

UPDATE ag.survey_question SET "spanish" = 'Por favor, califique la GRAVEDAD ACTUAL (ej., las últimas 2 SEMANAS) de cualquier dificultad para conciliar el sueño' WHERE survey_question_id = '229';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'None' -> 'Ninguno'
UPDATE ag.survey_response SET "spanish" = 'Leve' WHERE american = 'Mild';
-- responses exists, 'Moderate' -> 'Moderado'
UPDATE ag.survey_response SET "spanish" = 'Muy fuerte' WHERE american = 'Severe';
UPDATE ag.survey_response SET "spanish" = 'Muy Grave' WHERE american = 'Very Severe';

UPDATE ag.survey_question SET "spanish" = 'Por favor, califique la GRAVEDAD ACTUAL (ej., las últimas 2 SEMANAS) de cualquier dificultad para permanecer dormido' WHERE survey_question_id = '230';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'None' -> 'Ninguno'
-- responses exists, 'Mild' -> 'Leve'
-- responses exists, 'Moderate' -> 'Moderado'
-- responses exists, 'Severe' -> 'Muy fuerte'
-- responses exists, 'Very Severe' -> 'Muy Grave'

UPDATE ag.survey_question SET "spanish" = 'Por favor, califique la GRAVEDAD ACTUAL (ej., las últimas 2 SEMANAS) de despertar demasiado temprano' WHERE survey_question_id = '231';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'None' -> 'Ninguno'
-- responses exists, 'Mild' -> 'Leve'
-- responses exists, 'Moderate' -> 'Moderado'
-- responses exists, 'Severe' -> 'Muy fuerte'
-- responses exists, 'Very Severe' -> 'Muy Grave'

UPDATE ag.survey_question SET "spanish" = '¿Qué tan SATISFECHO/INSATISFECHO está con su patrón de sueño ACTUAL?' WHERE survey_question_id = '232';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'Muy Satisfecho' WHERE american = 'Very satisfied';
UPDATE ag.survey_response SET "spanish" = 'Satisfecho' WHERE american = 'Satisfied';
UPDATE ag.survey_response SET "spanish" = 'Moderadamente satisfecho' WHERE american = 'Moderately satisfied';
UPDATE ag.survey_response SET "spanish" = 'Insatisfecho' WHERE american = 'Dissatisfied';
UPDATE ag.survey_response SET "spanish" = 'Muy Insatisfecho' WHERE american = 'Very dissatisfied';

UPDATE ag.survey_question SET "spanish" = '¿Qué tan NOTORIO para los demás crees que tu problema de sueño es en términos de afectar la calidad de tu vida?' WHERE survey_question_id = '233';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Not at all' -> 'No en absoluto'
UPDATE ag.survey_response SET "spanish" = 'Apenas notorio' WHERE american = 'Barely noticeable';
UPDATE ag.survey_response SET "spanish" = 'Algo notorio' WHERE american = 'Somewhat noticeable';
UPDATE ag.survey_response SET "spanish" = 'Bastante notorio' WHERE american = 'Quite Noticeable';
UPDATE ag.survey_response SET "spanish" = 'Muy notorio' WHERE american = 'Very noticeable';

UPDATE ag.survey_question SET "spanish" = '¿Qué tan preocupado/afligido está acerca de su problema de sueño actual?' WHERE survey_question_id = '234';
-- responses exists, 'Unspecified' -> 'No especificado'
UPDATE ag.survey_response SET "spanish" = 'No preocupado' WHERE american = 'Not at all';
UPDATE ag.survey_response SET "spanish" = 'Un poco preocupado' WHERE american = 'A little worried';
UPDATE ag.survey_response SET "spanish" = 'Algo preocupado' WHERE american = 'Somewhat worried';
UPDATE ag.survey_response SET "spanish" = 'Bastante preocupado' WHERE american = 'Quite worried';
UPDATE ag.survey_response SET "spanish" = 'Muy preocupado' WHERE american = 'Very worried';

UPDATE ag.survey_question SET "spanish" = 'Hasta qué punto considera que su problema de sueño INTERFIERE con su funcionamiento diario (por ejemplo, fatiga diurna, estado de ánimo, capacidad para funcionar en el trabajo / tareas diarias, concentración, memoria, estado de ánimo, etc.)  ACTUALMENTE?' WHERE survey_question_id = '235';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Not at all' -> 'No en absoluto'
UPDATE ag.survey_response SET "spanish" = 'Interfiere algo' WHERE american = 'Interfering';
UPDATE ag.survey_response SET "spanish" = 'Interfiere un poco' WHERE american = 'Somewhat interfering';
UPDATE ag.survey_response SET "spanish" = 'Interfiere bastante' WHERE american = 'Quite interfering';
UPDATE ag.survey_response SET "spanish" = 'Interfiere mucho' WHERE american = 'Very interfering';

UPDATE ag.survey_question SET "spanish" = '¿Le ha ocurrido algo de lo siguiente a causa de Coronavirus/COVID-19? (marque todas las que correspondan)' WHERE survey_question_id = '238';
-- responses exists, 'Unspecified' -> 'No especificado'
-- responses exists, 'Fallen ill physically' -> 'Se enfermo físicamente'
-- responses exists, 'Hospitalized' -> 'Hospitalizado'
-- responses exists, 'Put into self-quarantine with symptoms' -> 'Puesto en cuarentena con síntomas'
-- responses exists, 'Put into self-quarantine without symptoms (e.g. due to possible exposure)' -> 'Puesto en cuarentena sin síntomas (por ejemplo, debido a una posible exposición)'
-- responses exists, 'Lost job' -> 'Perdida de Trabajo'
-- responses exists, 'Reduced ability to earn money' -> 'Reducción de la capacidad de ganar dinero'
-- responses exists, 'None of the above' -> 'Ninguno de los anteriores'

