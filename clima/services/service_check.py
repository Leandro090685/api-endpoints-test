from clima.models import Registros

class CheckService:
    def check(ciudad=None):
        mydata= Registros.objects.filter(city = ciudad).values()
        if mydata == []:
            pass
        else:
            Registros.objects.filter(city=ciudad).delete()
           

            


