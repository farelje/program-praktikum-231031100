
print('\n')
biodata = { 'nama'  : 'Muhammad Farel Shahizidan Lefrand',
'nim'   : '231031119',
'kelas' : 'S123D',
'jenis kelamin' : 'laki-laki',
'agama' : 'islam',
'umur': '18 tahun',
'email' : 'fawrrel@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)





