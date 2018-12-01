from jidelnicek import db

#creating model (=table)
class Recepty(db.Model):
			#overriding the default set up of database name
			__tablename__ = "recepty"
			id = db.Column(db.Integer, primary_key=True)
			url = db.Column(db.String(100))
			title = db.Column(db.String(64))
			foto = db.Column(db.String(100))

#nastavit relationship
# xyz = db.relationship('Tagy', backref='xzy', lazy=True)

##Neni nutne mit napsane
			def _init_(self,url,title,foto):

					self.url = url
					self.title = title
					self.foto = foto

			def __repr__(self):
					return f"Název receptu: {self.title} a URL: {self.url}"



class Ingredience(db.Model):

			__tablename__ = "ingredience"

			#jidelnicek = db.relationship(Jidelnicek)

			id = db.Column(db.Integer, db.ForeignKey('recepty.url'))
			ingredience = db.Column(db.String(100))
			nazev_ingredience = db.Column(db.String(30))

			def __init__(self,ingredience,nazev_ingredience):

					self.ingredience = ingredience
					self.nazev_ingredience = nazev_ingredience
			
			def __repr__(self):
					return f"Ingredience: {self.ingredience} a Název ingredience: {self.nazev_ingredience}"



class Tagy(db.Model):
		
			__tablename__ = "tagy"

			#jidelnicek = db.relationship(Jidelnicek)

			id = db.Column(db.Integer,db.ForeignKey('recepty.url'))
			nase_tagy = db.Column(db.String(20))

			def _init_(self,nase_tagy):

					self.nase_tagy = nase_tagy
			
			def __repr__(self):
					return f"K receptu {self.id} jsou přiřazeny tyto tagy: {self.nase_tagy}"
