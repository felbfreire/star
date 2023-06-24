import sqlalchemy


metadata = sqlalchemy.MetaData()

stars = sqlalchemy.Table(
        'stars',
        metadata,
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('star_name', sqlalchemy.String,),
        )
