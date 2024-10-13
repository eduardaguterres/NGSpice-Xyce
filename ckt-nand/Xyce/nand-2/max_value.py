import pandas as pd

# Carregar o arquivo CSV
file_path = 'nand-set.cir.csv'  # Substitua pelo caminho correto do arquivo
data = pd.read_csv(file_path)

# Encontrar o valor mínimo da tensão na coluna 'V(OUT)'
max_voltage_out = data['V(OUT)'].max()
max_time_out = data['TIME'][data['V(OUT)'].idxmax()]

# Exibir o resultado
print(f"A tensão máxima na coluna V(OUT) é {max_voltage_out} V e ocorre no tempo {max_time_out} segundos.")
