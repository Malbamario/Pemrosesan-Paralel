from mpi4py import MPI
comm = MPI.COMM_WORLD
if comm.rank==0:
    print("saya boss")
    data = {'nama':'Mario Alfredo Bawu'}
    comm.send(data, dest=1)
elif comm.rank==1:
    data = comm.recv(source=0)
    print(comm.Get_rank(), data['nama'])
else:
    print("saya anak buah no",comm.rank,"dari total",comm.size)
