#Nama : William Gunawan
#NIM  : 18220077
#Buat sebuah API menggunakan FastAPI yang fungsinya untuk menerima data NIM dan nama mahasiswa dari client. Data tersebut dikirim dalam format JSON dan disimpan oleh handler/function di dalam API tersebut ke dalam sebuah variabel (dictionary). 


from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

mahasiswa = {
    18220077 :{
    "Nama":"William Gunawan",
    "Fakultas":"STEI",
    "Jurusan":"STI"
    }
}
#buat class Mahasiswa
class Mahasiswa(BaseModel):
     Nama :str
     Fakultas :str
     Jurusan :str

@app.get("/")
def index():
    return {"name":"first data"}


@app.get("/get-mahasiswa/{mahasiwa_NIM}")
def get_mahasiswa(mahasiswa_NIM : int):
    return mahasiswa[mahasiswa_NIM]

@app.post("/create-mahasiswa/{mahasiswa_NIM}")
def create_mahasiswa(mahasiswa_NIM : int , student : Mahasiswa) :
    if mahasiswa_NIM in mahasiswa:
        return{"Error, mahasiswa sudah ada"}
    else:
        mahasiswa[mahasiswa_NIM]= student  #memasukkan data mahasiswa
        return mahasiswa[mahasiswa_NIM]

