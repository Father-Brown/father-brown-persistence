from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Relationship():
    E = 'E'    
    POR='POR'
    CITA = 'CITA'
    FONTE='FONTE'    
    E_FONTE='E_FONTE'
    PUBLICOU='PUBLICOU'
    PUBLICOU_NO='PUBLICOU_NO'
    CONHECIDO_COMO='CONHECIDO_COMO'

class Tipo(GraphObject):
    __primarykey__ = "description"
    description = Property()    
    news = RelatedFrom('News', Relationship.E)

class News(GraphObject):    
    title = Property()
    subTitle = Property()
    url = Property()
    datePublished = Property()
    site= RelatedFrom('Site', Relationship.PUBLICOU)
    autor= RelatedFrom('Autor', Relationship.POR)
    tipo = RelatedTo(Tipo, Relationship.E)
    fonte = RelatedTo('News', Relationship.FONTE)
    content = Property()

class Autor(GraphObject):
    __primarykey__ = "name"
    name = Property()    
    news = RelatedTo(News)
    site= RelatedFrom('Site', Relationship.PUBLICOU_NO)

class Site(GraphObject):
    __primarykey__ = "name"
    name = Property()
    url = Property()
    news = RelatedTo(News)
    # autor = RelatedTo(Autor)


