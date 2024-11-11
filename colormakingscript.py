import pandas as pd
rgb_values = []
complements = []

for r in range(0,256,10):  
    for g in range(0,256,10):
        for b in range(0,256,10):
            rgb = [r, g, b]
            complement = [255 - r, 255 - g, 255 - b]
            rgb_values.append(rgb)
            complements.append(complement)

data = {
    "RGB": rgb_values,
    "Complement": complements
}
#making it into dataframe
df = pd.DataFrame(data)
#making dataframe into excel
df.to_excel("colordataset.xlsx", index=False)

print("Excel sheet created successfully as colordataset.xlsx")