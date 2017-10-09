from django.conf.urls import url
from gpo.processo_pagamento.views import *

urlpatterns = [
    url(r'^processo_pagamento$', processo_pagamento, name='processo'),
    url(r'^processo_pagamento/add', criar_processo_pagamento, name='criar_processo'),

]
