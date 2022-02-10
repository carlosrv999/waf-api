# LLAMAR APIS HUAWEI CLOUD

## Pedir un token

Configurar las variables:

- domain_name
- username
- password
- project_id

El token se guardará en la variable **token**.

## Llamar al API de WAF

Dirigirse al siguiente link: https://support.huaweicloud.com/intl/en-us/api-waf/UpdatePolicyRuleStatus.html, cómo cambiar el estado de una regla, usar como endpoint el siguiente URL:

PUT /v1/{project_id}/waf/policy/{policy_id}/{ruletype}/{rule_id}/status.

En los headers poner el token, como el ejemplo de obtener una IP publica