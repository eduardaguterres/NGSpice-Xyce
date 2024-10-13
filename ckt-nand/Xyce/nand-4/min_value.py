import pandas as pd

# Carregar o arquivo CSV
file_path = 'nand-set.cir.csv'  # Substitua pelo caminho correto do arquivo
data = pd.read_csv(file_path)

# Encontrar o valor mínimo da tensão na coluna 'V(OUT)'
min_voltage_out = data['V(OUT)'].min()
min_time_out = data['TIME'][data['V(OUT)'].idxmin()]

# Exibir o resultado
print(f"A tensão mínima na coluna V(OUT) é {min_voltage_out} V e ocorre no tempo {min_time_out} segundos.")
