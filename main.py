import os
from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

load_dotenv()
 
QiskitRuntimeService.save_account(
  token=os.getenv("API_TOKEN_QUANTUM"),
  channel="ibm_quantum",
  overwrite=True
)

example_circuit = QuantumCircuit(2)
example_circuit.measure_all()
 
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
 
sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"job id: {job.job_id()}")