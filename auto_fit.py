import os, time

meses ={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}

def insertarArchivo(ruta, archivo):
    os.system("move "+os.getcwd()+"\\"+archivo+" "+ruta+"\\")

def insertarCarpeta(mes, anno, archivo):    
    nomDir = str(anno)+'_'+str(meses[mes])
    rutaDir = os.path.join(os.getcwd(),nomDir)
    
    if not os.path.exists(nomDir):
        os.mkdir(nomDir)
        insertarArchivo(rutaDir, archivo)        
    else:
        insertarArchivo(rutaDir, archivo)        

def propiedadFichero(file):
    (year, mon, mday, hour, min, sec, wday, yday, isdst) = time.gmtime(os.path.getmtime(file))
    insertarCarpeta(mon, year, file)   #print(f'{mon} {year}')


for f in os.listdir(os.getcwd()):
    if f.endswith('.pdf') or f.endswith('.csv') or f.endswith('.txt') or f.endswith('.xlsx') or f.endswith('.docx'):        
        archivo = f.replace(' ', '_')   #debemos reemplazar los espacios vacios ya que en consola reconoceria cada parte como un archivo separado
        os.rename(f, archivo)           #renombramos el archivo
        propiedadFichero(archivo)
        

