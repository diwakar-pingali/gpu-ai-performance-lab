import torch

#set the default device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#Initialise torch tensor of size 1024x1024
dim_x = 1024
dim_y = 1024
shape = (dim_x, dim_y)

start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)

tensor_a = torch.rand(shape, device=device)
tensor_b = torch.rand(shape, device=device)

start_event.record()
#Add the tensors on device
tensor_c = tensor_a + tensor_b
end_event.record()

torch.cuda.synchronize()

elapsed_time_ms = start_event.elapsed_time(end_event)


print(f"Execution time for the tensor stored on: {tensor_c.device} is {elapsed_time_ms:.2f} ms")


