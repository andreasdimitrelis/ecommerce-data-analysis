import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "ecommerce_db.csv"

# Φόρτωση CSV
df = pd.read_csv(file_path)

# Μετονομασία: η πρώτη στήλη είναι το προϊόν, η τελευταία το ποσό
df = df.rename(columns={
    df.columns[0]: 'Product',
    df.columns[-1]: 'OrderAmount'
})

# Αφαίρεση γραμμών χωρίς ποσό
df = df.dropna(subset=['OrderAmount'])

# Μετατροπή σε float
df['OrderAmount'] = pd.to_numeric(df['OrderAmount'], errors='coerce')

# Ξαναφιλτράρουμε NaN μετά τη μετατροπή
df = df.dropna(subset=['OrderAmount'])

# Υπολογισμοί
total_sales = df['OrderAmount'].sum()
avg_order_value = df['OrderAmount'].mean()
top_products = df.groupby('Product')['OrderAmount'].sum().sort_values(ascending=False).head(5)

# Εκτυπώσεις
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

print("💰 Συνολικές Πωλήσεις:", total_sales)
print("📊 Μέση Αξία Παραγγελίας:", avg_order_value)
print("🏆 Top 5 Προϊόντα:\n", top_products)

# Barplot για top προϊόντα
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 5 Προϊόντα")
plt.xlabel("Συνολικές Πωλήσεις (€)")
plt.ylabel("Προϊόν")
plt.show()

# Histogram για αξία παραγγελίας
plt.figure(figsize=(8,5))
sns.histplot(df['OrderAmount'], bins=20, kde=True, color="blue")
plt.title("Κατανομή Αξίας Παραγγελιών")
plt.xlabel("Αξία (€)")
plt.ylabel("Συχνότητα")
plt.show()

