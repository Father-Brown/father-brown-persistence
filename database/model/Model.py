from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo


class Tipo(GraphObject):
    __primarykey__ = "description"
    description = Property()
    news = RelatedFrom('News', 'E')

class News(GraphObject):
    __primarykey__ = "title"
    title = Property()
    subTitle = Property()
    url = Property()
    datePublished = Property()
    site= RelatedFrom('Site', 'PUBLICOU')
    autor= RelatedFrom('Autor', 'POR')
    tipo = RelatedTo(Tipo, 'E')
    content = Property()

class Autor(GraphObject):
    __primarykey__ = "name"
    name = Property()    
    news = RelatedTo(News)
    site= RelatedFrom('Site', 'PUBLICOU NO')

class Font(GraphObject):
    __primarykey__ = "name"
    name = Property()
    url = Property()
    news = RelatedTo(News)
    site= RelatedFrom('Site', 'PUBLICOU NO')

class Site(GraphObject):
    __primarykey__ = "name"
    name = Property()
    url = Property()
    news = RelatedTo(News)
    # autor = RelatedTo(Autor)


