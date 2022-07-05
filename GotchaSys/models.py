from django.db import models

class Games(models.Model):
	Genre = models.CharField(max_length=30)
	Release_Date = models.DateField()
	Game_Description = models.TextField(default="")

	#For Relationships#

	Game_ID = models.CharField(max_length=40, primary_key=True)

	def __str__(self):
		return self.Game_ID

class Feedback(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	number = models.IntegerField()
	query = models.TextField(default="")

	#For Relationships#

	User_ID = models.BigAutoField(primary_key=True)
	# User_Game = models.ManyToManyField(Games)

	def __str__(self):
		return self.name

class Gacha(models.Model):
	Banner_Type = models.CharField(max_length=20)
	Banner_Description = models.TextField(default="")
	Banner_ReleaseDate = models.DateField()
	Banner_EndDate = models.DateField()

	#For Relationships#

	Banner_ID = models.CharField(max_length=80, primary_key=True)
	Gacha_GameID = models.ForeignKey(Games, on_delete=models.CASCADE)

	def __str__(self):
		return self.Banner_ID

class Storylines(models.Model):

	Chapter_Description = models.TextField(default="")
	Chapter_Setting = models.TextField(default="")

	#For Relationships#

	Chapter_ID = models.CharField(max_length=70, primary_key=True)
	Story_GameID = models.ForeignKey(Games, on_delete=models.CASCADE)

	def __str__(self):
		return self.Chapter_ID

class Characters(models.Model):
	
	Character_Rarity = models.IntegerField()
	Char_Description = models.TextField(default="")

	#For Relationships#

	Character_ID = models.CharField(max_length=50, primary_key=True)
	Char_GameID = models.ForeignKey(Games, on_delete=models.CASCADE)
	Char_GachaID = models.ForeignKey(Gacha, on_delete=models.CASCADE)
	Char_StoryID = models.ForeignKey(Storylines, on_delete=models.CASCADE)

	def __str__(self):
		return self.Character_ID

class CharType(models.Model):
	  Char_Range = models.CharField(max_length=25)
	  Class_Desc = models.TextField(default="")
	  Pref_Gear = models.TextField(default="")

	  #For Relationships#

	  CharClass = models.CharField(max_length=30, primary_key=True)
	  CharType_CharID = models.OneToOneField(Characters, on_delete=models.CASCADE)
	  CharType_GameID = models.ForeignKey(Games, on_delete=models.CASCADE)

	  def __str__(self):
	  	return self.CharClass

class Equipment(models.Model):
	  
	  Equip_Weapons = models.TextField(default="")
	  Equip_Essentials = models.TextField(default="")
	  Other_Equip = models.TextField(default="")

	  #For Relationships#

	  EquipID = models.CharField(max_length=45, primary_key=True)
	  Equip_GameID = models.ForeignKey(Games, on_delete=models.CASCADE)
	  Equip_CharID = models.ForeignKey(Characters, on_delete=models.CASCADE)
	  Equip_CharType = models.ForeignKey(CharType, on_delete=models.CASCADE)
	  Equip_Story = models.ForeignKey(Storylines, on_delete=models.CASCADE)

	  def __str__(self):
	  	return self.EquipID

# Create your models here.
