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
			ingredience = db.relationship('Ingredience', backref='recepty', lazy='dynamic')
			tagy = db.relationship('Tagy', backref='recepty', lazy='dynamic')

			def _init_(self,url,title,foto):

					self.url = url
					self.title = title
					self.foto = foto 

			def __repr__(self):
					return f"{self.title}"



class Ingredience(db.Model):

			__tablename__ = "ingredience"

			#jidelnicek = db.relationship(Jidelnicek)

			id = db.Column(db.Integer, primary_key=True)
			ingredience = db.Column(db.String(100))
			nazev_ingredience = db.Column(db.String(30))
			recepty_id = db.Column(db.Integer, db.ForeignKey('recepty.id') )

			def __init__(self,ingredience,nazev_ingredience):

					self.ingredience = ingredience
					self.nazev_ingredience = nazev_ingredience
			
			def __repr__(self):
					return f"{self.ingredience}"



class Tagy(db.Model):
		
			__tablename__ = "tagy"

			#jidelnicek = db.relationship(Jidelnicek)

			id = db.Column(db.Integer, primary_key=True)	
			nase_tagy = db.Column(db.String(20))
			recepty_id = db.Column(db.Integer, db.ForeignKey('recepty.id') )

			def _init_(self,nase_tagy):

					self.nase_tagy = nase_tagy
			
			def __repr__(self):
					return f"K receptu {self.id} jsou přiřazeny tyto tagy: {self.nase_tagy}"
