"""from jidelnicek import db

#creating model (=table)
class Jidelnicek(db.Model):
			#overriding the default set up of database name
			__tablename__ = "jidelnicek"
			id = db.Column(db.Integer)
			url = db.Column(db.String(100),primary_key=True,unique=True)
			title = db.Column(db.String(64))
			foto = db.Column(db.String(100))
			ingredience = db.Column(db.String(64))
			nazev_ingredience = db.Column(db.String(20))

#nastavit relationship
# xyz = db.relationship('Tagy', backref='xzy', lazy=True)

##Neni nutne mit napsane
			def _init_(self,url,title,foto,ingredience,nazev_ingredience):
					#super.__init__(self)

					self.url = url
					self.title = title
					self.foto = foto
					self.ingredience = ingredience
					self.nazev_ingredience = nazev_ingredience

			def __repr__(self):
					return f"Název receptu: {self.title} a URL: {self.url}"


class Tagy(db.Model):
		
			__tablename__ = "tagy"

			#jidelnicek = db.relationship(Jidelnicek)

			id = db.Column(db.Integer,primary_key=True)
			url = db.Column(db.String(100),unique=True,db.ForeignKey('jidelnicek.url'))
			tags = db.Column(db.String(20)
			title = db.Column(db.String(64))
			nase_tagy = db.Column(db.String(20))

			def _init_(self,url,tags,title,nase_tagy):

					self.url = url
					self.tags = tags
					self.title = title
					self.nase_tagy = nase_tagy
			
			def __repr__(self):
					return f"K receptu {self.title} jsou přiřazeny tyto tagy: {self.nase_tagy}"
"""