from .models import *



class GPOChoices:

    #Natureza da Despesa(Processos de Pagamento)
    DIARIAS_CIVIL = u'Diárias [33.90.14.00'
    MATERIAL_DE_CONSUMO = u'Materia de Consumo [33.90.30.00]'
    OUTROS_SERVICOS_TERCEIROS_PESSOA_FISICA = u'Serviços de Pessoa Física [33.90.36.00]'
    OUTROS_SERVICOS_TERCEIROS_PESSOA_JURIDICA = u'Serviços de Pessoa Jurídica [33.90.39.00]'


    NATUREZA_DA_DESPESA = {
        DIARIAS_CIVIL : u'Diárias [33.90.14.00',
        MATERIAL_DE_CONSUMO : u'Materia de Consumo [33.90.30.00]',
        OUTROS_SERVICOS_TERCEIROS_PESSOA_FISICA : u'Serviços de Pessoa Física [33.90.36.00]',
        OUTROS_SERVICOS_TERCEIROS_PESSOA_JURIDICA : u'Serviços de Pessoa Jurídica [33.90.39.00]',
    }


    #Municípios da Paraíba
    AGUA_BRANCA = u'Agua_Branca'
    AGUIAR = u'Aguiar'
    ALAGOA_GRANDE = u'Alagoa Grande'
    ALAGOA_NOVA = u'Alagoa Nova'
    ALAGOINHA = u'Alagoinha'
    ALCANTIL = u'Alcantil'
    LAGODAO_JANDIRA = u'Algodão de Jandaira'
    ALHANDRA = u'Alhandra'
    AMPARO = u'Amparo'
    APARECIDA = u'Aparecida'
    ARACAGI = u'Aracagi'
    ARARA = u'Arara'
    ARARUNA = u'Araruna'
    AREIA_DE_BARAUNA = u'Areia de Baraunas'
    AREIA = u'Areia'
    AREIAL = u'Areial'
    AROEIRA = u'Aroeiras'
    ASSUNCAO = u'Assuncao'
    BAIA_DA_TRAICAO = u'Baia da Traicao'
    BANANEIRAS = u'Bananeiras'
    BARAUNA = u'Barauna'
    BARRA_SANTA_ROSA = u'Barra de Santa Rosa'
    BARRA_DE_SANTANA = u'Barra de Santana'
    BARRA_DE_SAO_MIGUEL = u'Barra de São Miguel'
    MAYEUX = u'Bayeux'
    BELEM_BREJO_DO_CRUZ = u'Belem do Brejo do Cruz'
    BELEM = u'Belem'
    BERNADINO_BATISTA = u'Bernardino Batista'
    BOA_VENTURA = u'Boa Ventura'
    BOA_VISTA = u'Boa Vista'
    BOM_JESUS = u'Bom Jesus'
    BOM_SUCESSO = u'Bom Sucesso'
    BONITO_SANTA_FE = u'Bonito de Santa Fé'
    BOQUEIRAO = u'Boqueirão'
    BORBOREMA = u'Borborema'
    BREJO_DO_CRUZ = u'Brejo do Cruz'
    BREJO_DOS_SANTOS = u'Brejo dos Santos'
    CAAPORA = u'Caaporã'
    CABACEIRAS = u'Cabaceiras'
    CABEDELO = u'Cabedelo'
    CACHOEIRA_DOS_INDIOS = u'Cachoeira dos Índios'
    CACIMBRA_DE_AREIA = u'Cacimba de Areia'
    CACIMBRA_DE_DENTRO = u'Cacimba de Dentro'
    CACIMBRAS = u'Cacimbas'
    CAICARA = u'Caiçara'
    CAJAZEIRAS = u'Cajazeiras'
    CAJAZEIRINHAS = u'Cajazeirinhas'
    CALDAS_BRANDAO = u'Caldas Brandão'
    CAMALAU = u'Camalaú'
    CAMPINA_GRANDE = u'Campina Grande'
    CAPIM = u'Capim'
    CARAUBAS = u'Caraubas'
    CARRAPATEIRA = u'Carrapateira'
    CASSERENGUE = u'Casserengue'
    CATINGUEIRA = u'Catingueira'
    CATOLE_DO_ROCHA = u'Catole do Rocha'
    CATURITE = u'Caturite'
    CONCEICAO = u'Conceição'
    CONDADO = u'Condado'
    CONDE = u'Conde'
    CONGO = u'Congo'
    COREMAS = u'Coremas'
    COXIXOLA = u'Coxixola'
    CRUZ_DO_ESPIRITO_SANTO = u'Cruz do Espirito Santo'
    CUBATI = u'Cubati'
    CUITE_DE_MAMAGUAPE = u'Cuité de Mamanguape'
    CUITE = u'Cuité'
    CUITEGI = u'Cuitegi'
    CURRAL_VELHO = u'Curral Velho'
    CURRAL_DE_CIMA = u'Curral de Cima'
    DAMIAO = u'Damião'
    DESTERRO = u'Desterro'
    DIAMANTE = u'Diamante'
    DONA_INES = u'Dona Inês'
    DUAS_ESTRADAS = u'Duas Estradas'
    EMAS = u'Emas'
    ESPERANCA = u'Esperança'
    FAGUNDES = u'Fagundes'
    FREI_MARTINHO = u'Frei Martinho'
    GADO_BRAVO = u'Gado Bravo'
    GUARABIRA = u'Guarabira'
    GURINHEM = u'Gurinhem'
    GURJAO = u'Gurjão'
    IBIARA = u'Ibiara'
    IGUARACY = u'Igaracy'
    IMACULADA = u'Imaculada'
    INGA = u'Inga'
    ITABAIANA = u'Itabaiana'
    ITAPORANGA = u'Itaporanga'
    ITAPOROROCA = u'Itapororoca'
    ITATUBA = u'Itatuba'
    JACARAU = u'Jacarau'
    JERICO = u'Jericó'
    JOAO_PESSOA = u'João Pessoa'
    JUAREZ_TAVORA = u'Juarez Tavora'
    JUAZEIRINHO = u'Juazeirinho'
    JUNCO_DO_SERIDO = u'Junco do Serido'
    JURIPIRANGA = u'Juripiranga'
    JURU = u'Juru'
    LAGOA_SECA = u'Lagoa Seca'
    LAGOA_DE_DENTRO = u'Lagoa de Dentro'
    LAGOA_LASTRO = u'Lagoa Lastro'
    LIVRAMENTO = u'Livramento'
    LOGRADOURO = u'Logradouro'
    LUCENA = u'Lucena'
    MAE_DAGUA = u'Mae dAgua'
    MALTA = u'Malta'
    MAMANGUAPE = u'Mamanguape'
    MANAIRA = u'Manaira'
    MARCACAO = u'Marcação'
    MARI = u'Mari'
    MARIZOPOLIS = u'Marizopolis'
    MASSARANDUBA = u'Massaranduba'
    MATARACA = u'Mataraca'
    MATINHA = u'Matinhas'
    MATO_GROSSO = u'Mato Grosso'
    MATUREIA = u'Matureia'
    MOGEIRO = u'Mogeiro'
    MONTADAS = u'Montadas'
    MONTE_HOREBE = u'Monte Horebe'
    MONTEIRO = u'Monteiro'
    MULUNGU = u'Mulungu'
    NATUBA = u'Natuba'
    NAZAREZINHO = u'Nazarezinho'
    NOVA_FLORESTA = u'Nova Floresta'
    NOVA_OLINDA = u'Nova Olinda'
    NOVA_PALMEIRA = u'Nova Palmeira'
    OLHO_DAGUA = u'Olho dAgua'
    OLIVEDOS = u'Olivedos'
    OURO_VELHO = u'Ouro Velho'
    PARARI = u'Parari'
    PASSAGEM = u'Passagem'
    PATOS = u'Patos'
    PAULISTA = u'Paulista'
    PEDRA_BRANCA = u'Pedra Branca'
    PEDRA_LAVRADA = u'Pedra Lavrada'
    PEDRA_DE_FOGO = u'Pedras de Fogo'
    PEDRO_REGIO = u'Pedro Regio'
    PIANCO = u'Piancó'
    PICUI = u'Picuí'
    PILAR = u'Pilar'
    PILOES = u'Pilões'
    PILOEZINHOS = u'Pilõezinhos'
    PIRPIRITUBA = u'Pirpirituba'
    PITIBU = u'Pitimbu'
    POCINHOS = u'Pocinhos'
    POCO_DANTAS = u'Poco Dantas'
    POCO_DE_JOSE_DE_MOURA = u'Poço de José de Moura'
    POMBAL = u'Pombal'
    PRATA = u'Prata'
    PRINCESA_ISABEL = u'Princesa Isabel'
    PUXINANA = u'Puxinanã'
    QUEIMADAS = u'Queimadas'
    QUIXABA = u'Quixaba'
    REMIGIO = U'Remigio'
    RIACAO_DO_BACAMARTE = u'Riachão do Bacamarte'
    RIACHO_DO_POCO = u'Riachao do Poço'
    SALGADO_DE_SAO_FELIX = u'Salgado de São Felix'
    RIACAO = u'Riachão'
    RIACHO_DE_SANTO_ANTONIO = u'Riacho de Santo Antonio'
    RIACHO_DOS_CAVALOS = u'Riacho dos Cavalos'
    RIO_TINTO = u'Rio Tinto'
    SALGADINHO = u'Salgadinho'
    SANTA_CECILIA = u'Santa Cecilia'
    SANTA_CRUZ = u'Santa Cruz'
    SANTA_HELENA = u'Santa Helena'
    SANTA_INES = u'Santa Inês'
    SANTA_LUZIA = u'Santa Luzia'
    SANTA_RITA = u'Santa Rita'
    SANTA_TERESINHA = u'Santa Teresinha'
    SANTANA_DE_MANGUEIRA = u'Santana de Mangueira'
    SANTANA_DOS_GARROTES = u'Santana dos Garrotes'
    SANTAREM = u'Santarem'
    SANTO_ANDRES = u'Santo Andre'
    SAO_BENTO_DE_POMBAL = u'São Bento de Pombal'
    SAO_BENTO = u'São Bento'
    SAO_DOMINGOS_DE_POMBAL = u'São Domingos de Pombal'
    SAO_DOMINGOS_DO_CARIRI = u'São Domingos do Cariri'
    SAO_FRANCISCO = u'São Francisco'
    SAO_JOAO_DO_CARIRI = u'São João do Cariri'
    SAO_JOAO_DO_RIO_DO_PEIXE = u'São João do Rio do Peixe'
    SAO_JOAO_DO_TIGRE = u'São João do Tigre'
    SAO_JOASE_DA_LAGOA_TAPADA = u'São José da Lagoa Tapada'
    SAO_JOSE_DE_CAIANA = u'São José de Caiana'
    SAO_JOSE_DE_ESPINHARAS = u'São José de Espinharas'
    SAO_JOSE_DE_PIRANHAS = u'São José de Piranhas'
    SAO_JOSE_DE_PRINCESA = u'São José de Princesa'
    SAO_JOSE_DO_BONFIM = u'São José do Bonfim'
    SAO_JOSE_DO_BREJO_DO_CRUZ = u'São José do Brejo do Cruz'
    SAO_JOSE_DO_SABUGI = u'SÃO José do Sabugi'
    SAO_JOSE_DOS_CORDEIROS = u'São José dos Cordeiros'
    SAO_JOSE_DOS_RAMOS = u'São José dos Ramos'
    SAO_MAMEDE = u'São Mamede'
    SAO_MIGUEL_DE_TAIPU = u'São Miguel de Taipu'
    SAO_SEBASTIAO_DE_LAGOA_DE_ROCA = u'São Sebastiao de Lagoa de Roça'
    SAO_SEBASTIAO_DO_UMBUZEIRO = u'São Sebastiao do Umbuzeiro'
    SAPE = u'Sapé'
    SERIDO =u'Serido'
    SERRA_BRANCA = u'Serra Branca'
    SERRA_GRANDE = u'Serra Grande'
    SERRA_REDONDA = u'Serra Redonda'
    SERRA_DA_RAIZ = u'Serra da Raiz'
    SERRARIA = u'Serraria'
    SERTAOZINHO = u'Sertãozinho'
    SOBRADO = u'Sobrado'
    SOLANEA = u'Solanea'
    SOLEDADE = u'Soledade'
    SOSSEGO = u'Sossego'
    SOUSA = u'Sousa'
    SUME = u'Sumé'
    TACIMA = u'Tacima'
    TAPEROA = u'Taperoá'
    TAVARES = u'Tavares'
    TEIXEIRA = u'Teixeira'
    TENORIO = u'Tenorio'
    TRIUNFO = u'Triunfo'
    UIRAUNA = u'Uirauna'
    UMBUZEIRO = u'Umbuzeiro'
    VAZEA = u'Varzea'
    VIEIROPOLIS = u'Vieiropolis'
    VISTA_SERRANA = u'Vista Serrana'
    ZABELE = u'Zabelê'


    MUNICIPIOS_PARAIBA = {

        AGUA_BRANCA : u'Agua_Branca',
        AGUIAR : u'Aguiar',
        ALAGOA_GRANDE : u'Alagoa Grande',
        ALAGOA_NOVA : u'Alagoa Nova',
        ALAGOINHA : u'Alagoinha',
        ALCANTIL : u'Alcantil',
        LAGODAO_JANDIRA : u'Algodão de Jandaira',
        ALHANDRA : u'Alhandra',
        AMPARO : u'Amparo',
        APARECIDA : u'Aparecida',
        ARACAGI : u'Aracagi',
        ARARA : u'Arara',
        ARARUNA : u'Araruna',
        AREIA_DE_BARAUNA : u'Areia de Baraunas',
        AREIA : u'Areia',
        AREIAL : u'Areial',
        AROEIRA : u'Aroeiras',
        ASSUNCAO : u'Assuncao',
        BAIA_DA_TRAICAO : u'Baia da Traicao',
        BANANEIRAS : u'Bananeiras',
        BARAUNA : u'Barauna',
        BARRA_SANTA_ROSA : u'Barra de Santa Rosa',
        BARRA_DE_SANTANA : u'Barra de Santana',
        BARRA_DE_SAO_MIGUEL : u'Barra de São Miguel',
        MAYEUX : u'Bayeux',
        BELEM_BREJO_DO_CRUZ : u'Belem do Brejo do Cruz',
        BELEM : u'Belem',
        BERNADINO_BATISTA : u'Bernardino Batista',
        BOA_VENTURA : u'Boa Ventura',
        BOA_VISTA : u'Boa Vista',
        BOM_JESUS : u'Bom Jesus',
        BOM_SUCESSO : u'Bom Sucesso',
        BONITO_SANTA_FE : u'Bonito de Santa Fé',
        BOQUEIRAO : u'Boqueirão',
        BORBOREMA : u'Borborema',
        BREJO_DO_CRUZ : u'Brejo do Cruz',
        BREJO_DOS_SANTOS : u'Brejo dos Santos',
        CAAPORA : u'Caaporã',
        CABACEIRAS : u'Cabaceiras',
        CABEDELO : u'Cabedelo',
        CACHOEIRA_DOS_INDIOS : u'Cachoeira dos Índios',
        CACIMBRA_DE_AREIA : u'Cacimba de Areia',
        CACIMBRA_DE_DENTRO : u'Cacimba de Dentro',
        CACIMBRAS : u'Cacimbas',
        CAICARA : u'Caiçara',
        CAJAZEIRAS : u'Cajazeiras',
        CAJAZEIRINHAS : u'Cajazeirinhas',
        CALDAS_BRANDAO : u'Caldas Brandão',
        CAMALAU : u'Camalaú',
        CAMPINA_GRANDE : u'Campina Grande',
        CAPIM : u'Capim',
        CARAUBAS : u'Caraubas',
        CARRAPATEIRA : u'Carrapateira',
        CASSERENGUE : u'Casserengue',
        CATINGUEIRA : u'Catingueira',
        CATOLE_DO_ROCHA : u'Catole do Rocha',
        CATURITE : u'Caturite',
        CONCEICAO : u'Conceição',
        CONDADO : u'Condado',
        CONDE : u'Conde',
        CONGO : u'Congo',
        COREMAS : u'Coremas',
        COXIXOLA : u'Coxixola',
        CRUZ_DO_ESPIRITO_SANTO : u'Cruz do Espirito Santo',
        CUBATI : u'Cubati',
        CUITE_DE_MAMAGUAPE : u'Cuité de Mamanguape',
        CUITE : u'Cuité',
        CUITEGI : u'Cuitegi',
        CURRAL_VELHO : u'Curral Velho',
        CURRAL_DE_CIMA : u'Curral de Cima',
        DAMIAO : u'Damião',
        DESTERRO : u'Desterro',
        DIAMANTE : u'Diamante',
        DONA_INES : u'Dona Inês',
        DUAS_ESTRADAS : u'Duas Estradas',
        EMAS : u'Emas',
        ESPERANCA : u'Esperança',
        FAGUNDES : u'Fagundes',
        FREI_MARTINHO : u'Frei Martinho',
        GADO_BRAVO : u'Gado Bravo',
        GUARABIRA : u'Guarabira',
        GURINHEM : u'Gurinhem',
        GURJAO : u'Gurjão',
        IBIARA : u'Ibiara',
        IGUARACY : u'Igaracy',
        IMACULADA : u'Imaculada',
        INGA : u'Inga',
        ITABAIANA : u'Itabaiana',
        ITAPORANGA : u'Itaporanga',
        ITAPOROROCA : u'Itapororoca',
        ITATUBA : u'Itatuba',
        JACARAU : u'Jacarau',
        JERICO : u'Jericó',
        JOAO_PESSOA : u'João Pessoa',
        JUAREZ_TAVORA : u'Juarez Tavora',
        JUAZEIRINHO : u'Juazeirinho',
        JUNCO_DO_SERIDO : u'Junco do Serido',
        JURIPIRANGA : u'Juripiranga',
        JURU : u'Juru',
        LAGOA_SECA : u'Lagoa Seca',
        LAGOA_DE_DENTRO : u'Lagoa de Dentro',
        LAGOA_LASTRO : u'Lagoa Lastro',
        LIVRAMENTO : u'Livramento',
        LOGRADOURO : u'Logradouro',
        LUCENA : u'Lucena',
        MAE_DAGUA : u'Mae dAgua',
        MALTA : u'Malta',
        MAMANGUAPE : u'Mamanguape',
        MANAIRA : u'Manaira',
        MARCACAO : u'Marcação',
        MARI : u'Mari',
        MARIZOPOLIS : u'Marizopolis',
        MASSARANDUBA : u'Massaranduba',
        MATARACA : u'Mataraca',
        MATINHA : u'Matinhas',
        MATO_GROSSO : u'Mato Grosso',
        MATUREIA : u'Matureia',
        MOGEIRO : u'Mogeiro',
        MONTADAS : u'Montadas',
        MONTE_HOREBE : u'Monte Horebe',
        MONTEIRO : u'Monteiro',
        MULUNGU : u'Mulungu',
        NATUBA : u'Natuba',
        NAZAREZINHO : u'Nazarezinho',
        NOVA_FLORESTA : u'Nova Floresta',
        NOVA_OLINDA : u'Nova Olinda',
        NOVA_PALMEIRA : u'Nova Palmeira',
        OLHO_DAGUA : u'Olho dAgua',
        OLIVEDOS : u'Olivedos',
        OURO_VELHO : u'Ouro Velho',
        PARARI : u'Parari',
        PASSAGEM : u'Passagem',
        PATOS : u'Patos',
        PAULISTA : u'Paulista',
        PEDRA_BRANCA : u'Pedra Branca',
        PEDRA_LAVRADA : u'Pedra Lavrada',
        PEDRA_DE_FOGO : u'Pedras de Fogo',
        PEDRO_REGIO : u'Pedro Regio',
        PIANCO : u'Piancó',
        PICUI : u'Picuí',
        PILAR : u'Pilar',
        PILOES : u'Pilões',
        PILOEZINHOS : u'Pilõezinhos',
        PIRPIRITUBA : u'Pirpirituba',
        PITIBU : u'Pitimbu',
        POCINHOS : u'Pocinhos',
        POCO_DANTAS : u'Poco Dantas',
        POCO_DE_JOSE_DE_MOURA : u'Poço de José de Moura',
        POMBAL : u'Pombal',
        PRATA : u'Prata',
        PRINCESA_ISABEL : u'Princesa Isabel',
        PUXINANA : u'Puxinanã',
        QUEIMADAS : u'Queimadas',
        QUIXABA : u'Quixaba',
        REMIGIO : u'Remigio',
        RIACAO_DO_BACAMARTE : u'Riachão do Bacamarte',
        RIACHO_DO_POCO : u'Riachao do Poço',
        RIACAO : u'Riachão',
        RIACHO_DE_SANTO_ANTONIO : u'Riacho de Santo Antonio',
        RIACHO_DOS_CAVALOS : u'Riacho dos Cavalos',
        RIO_TINTO : u'Rio Tinto',
        SALGADINHO : u'Salgadinho',
        SALGADO_DE_SAO_FELIX : u'Salgado de São Felix',
        SANTA_CECILIA : u'Santa Cecilia',
        SANTA_CRUZ : u'Santa Cruz',
        SANTA_HELENA : u'Santa Helena',
        SANTA_INES : u'Santa Inês',
        SANTA_LUZIA : u'Santa Luzia',
        SANTA_RITA : u'Santa Rita',
        SANTA_TERESINHA : u'Santa Teresinha',
        SANTANA_DE_MANGUEIRA : u'Santana de Mangueira',
        SANTANA_DOS_GARROTES : u'Santana dos Garrotes',
        SANTAREM : u'Santarem',
        SANTO_ANDRES : u'Santo Andre',
        SAO_BENTO : u'São Bento de Pombal',
        SAO_BENTO : u'São Bento',
        SAO_DOMINGOS_DE_POMBAL : u'São Domingos de Pombal',
        SAO_DOMINGOS_DO_CARIRI : u'São Domingos do Cariri',
        SAO_FRANCISCO : u'São Francisco',
        SAO_JOAO_DO_CARIRI : u'São João do Cariri',
        SAO_JOAO_DO_RIO_DO_PEIXE : u'São João do Rio do Peixe',
        SAO_JOAO_DO_TIGRE : u'São João do Tigre',
        SAO_JOASE_DA_LAGOA_TAPADA : u'São José da Lagoa Tapada',
        SAO_JOSE_DE_CAIANA : u'São José de Caiana',
        SAO_JOSE_DE_ESPINHARAS : u'São José de Espinharas',
        SAO_JOSE_DE_PIRANHAS : u'São José de Piranhas',
        SAO_JOSE_DE_PRINCESA : u'São José de Princesa',
        SAO_JOSE_DO_BONFIM : u'São José do Bonfim',
        SAO_JOSE_DO_BREJO_DO_CRUZ : u'São José do Brejo do Cruz',
        SAO_JOSE_DO_SABUGI : u'SÃO José do Sabugi',
        SAO_JOSE_DOS_CORDEIROS : u'São José dos Cordeiros',
        SAO_JOSE_DOS_RAMOS : u'São José dos Ramos',
        SAO_MAMEDE : u'São Mamede',
        SAO_MIGUEL_DE_TAIPU : u'São Miguel de Taipu',
        SAO_SEBASTIAO_DE_LAGOA_DE_ROCA : u'São Sebastiao de Lagoa de Roça',
        SAO_SEBASTIAO_DO_UMBUZEIRO : u'São Sebastiao do Umbuzeiro',
        SAPE : u'Sapé',
        SERIDO : u'Serido',
        SERRA_BRANCA : u'Serra Branca',
        SERRA_GRANDE : u'Serra Grande',
        SERRA_REDONDA : u'Serra Redonda',
        SERRA_DA_RAIZ : u'Serra da Raiz',
        SERRARIA : u'Serraria',
        SERTAOZINHO : u'Sertãozinho',
        SOBRADO : u'Sobrado',
        SOLANEA : u'Solanea',
        SOLEDADE : u'Soledade',
        SOSSEGO : u'Sossego',
        SOUSA : u'Sousa',
        SUME : u'Sumé',
        TACIMA : u'Tacima',
        TAPEROA : u'Taperoá',
        TAVARES : u'Tavares',
        TEIXEIRA : u'Teixeira',
        TENORIO : u'Tenorio',
        TRIUNFO : u'Triunfo',
        UIRAUNA : u'Uirauna',
        UMBUZEIRO : u'Umbuzeiro',
        VAZEA : u'Varzea',
        VIEIROPOLIS : u'Vieiropolis',
        VISTA_SERRANA : u'Vista Serrana',
        ZABELE : u'Zabelê',
    }