from mpi4py import MPI
comm = MPI.COMM_WORLD
# if comm.rank==0:
#     print("saya boss")
#     data = {'nama':'Mario Alfredo Bawu'}
#     comm.send(data, dest=1)
# elif comm.rank==1:
#     data = comm.recv(source=0)
#     print(comm.Get_rank(), data['nama'])
# else:
#     print("saya anak buah no",comm.rank,"dari total",comm.size)

match comm.rank:
    case 0:
        data = {'nama':'Mario Alfredo Bawu'}
        comm.send(data, dest=1)
        data = comm.recv(source=4)
        print(comm.Get_rank(), data['nama'])
    case 1:
        data = {'nama':'Ghifary Ahada Azra'}
        comm.send(data, dest=2)
        data = comm.recv(source=0)
        print(comm.Get_rank(), data['nama'])
    case 2:
        data = {'nama':'Afrizki Agi Datulmizan'}
        comm.send(data, dest=3)
        data = comm.recv(source=1)
        print(comm.Get_rank(), data['nama'])
    case 3:
        data = {'nama':'Elvita wilia kartika'}
        comm.send(data, dest=4)
        data = comm.recv(source=2)
        print(comm.Get_rank(), data['nama'])
    case 4:
        data = {'nama':'M. Afdhol Gilman'}
        comm.send(data, dest=0)
        data = comm.recv(source=3)
        print(comm.Get_rank(), data['nama'])
    case _:
        print(comm.rank, "Out of Case")