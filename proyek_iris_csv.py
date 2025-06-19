import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def jalankan_klasifikasi_dari_csv(nama_file_csv='Iris.csv'):
 
    try:
        df = pd.read_csv(nama_file_csv)
        print(f"✅ Berhasil memuat data dari '{nama_file_csv}'.")
    except FileNotFoundError:
        print(f"❌ ERROR: File '{nama_file_csv}' tidak ditemukan!")
        print("Pastikan file CSV berada di dalam folder yang sama dengan skrip Python ini.")
        return 

    if 'Id' in df.columns:
        df = df.drop('Id', axis=1)

    X = df.drop('Species', axis=1)
    
    y_str = df['Species']

    le = LabelEncoder()
    y = le.fit_transform(y_str)
    
    print("✅ Berhasil melakukan transformasi label (Teks -> Angka).")


    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"✅ Data telah dibagi: {len(X_train)} data latih dan {len(X_test)} data uji.")

 
    k = 5
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    print(f"✅ Model k-NN dengan k={k} berhasil dilatih.")


    y_pred = knn_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print("\n===== HASIL PREDIKSI PADA DATA UJI =====")
    for i in range(len(X_test)):
        data_asli = X_test.iloc[i] 
 
        prediksi_str = le.inverse_transform([y_pred[i]])[0]
        sebenarnya_str = le.inverse_transform([y_test[i]])[0]
        
        status = "✅" if prediksi_str == sebenarnya_str else "❌"
        print(f"Data Uji #{i+1}: Prediksi='{prediksi_str}', Sebenarnya='{sebenarnya_str}' {status}")
    
    print(f"\n===== AKURASI MODEL =====")
    print(f"Akurasi Model pada Data Uji: {accuracy * 100:.2f}%")


if __name__ == "__main__":
    jalankan_klasifikasi_dari_csv()