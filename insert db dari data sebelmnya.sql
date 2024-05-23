-- 2019 copy dari 2018
INSERT INTO isi (instansi, indikator, year, value)
SELECT 
    i_2018.instansi,
    i_2018.indikator,
    2019 AS year,  -- Tahun yang ingin Anda sisipkan jika data tahun sebelumnya tidak ada
    COALESCE(i_2019.value, i_2018.value) AS value  -- Mengambil nilai dari tahun sebelumnya jika data tidak ada untuk tahun yang diinginkan
FROM isi i_2018
LEFT JOIN isi i_2019 ON i_2018.instansi = i_2019.instansi AND i_2018.indikator = i_2019.indikator AND i_2019.year = 2019
WHERE i_2018.year = 2018
  AND i_2019.value IS NULL; -- Memeriksa apakah data untuk tahun yang diinginkan sudah ada
-- 2020 copy dari 2019
INSERT INTO isi (instansi, indikator, year, value)
SELECT 
    i_2019.instansi,
    i_2019.indikator,
    2020 AS year,  -- Tahun yang ingin Anda sisipkan jika data tahun sebelumnya tidak ada
    COALESCE(i_2020.value, i_2019.value) AS value  -- Mengambil nilai dari tahun sebelumnya jika data tidak ada untuk tahun yang diinginkan
FROM isi i_2019
LEFT JOIN isi i_2020 ON i_2019.instansi = i_2020.instansi AND i_2019.indikator = i_2020.indikator AND i_2020.year = 2020
WHERE i_2019.year = 2019
  AND i_2020.value IS NULL; -- Memeriksa apakah data untuk tahun yang diinginkan sudah ada
-- 2021 copy dari 2020
INSERT INTO isi (instansi, indikator, year, value)
SELECT 
    i_2020.instansi,
    i_2020.indikator,
    2021 AS year,  -- Tahun yang ingin Anda sisipkan jika data tahun sebelumnya tidak ada
    COALESCE(i_2021.value, i_2020.value) AS value  -- Mengambil nilai dari tahun sebelumnya jika data tidak ada untuk tahun yang diinginkan
FROM isi i_2020
LEFT JOIN isi i_2021 ON i_2020.instansi = i_2021.instansi AND i_2020.indikator = i_2021.indikator AND i_2021.year = 2021
WHERE i_2020.year = 2020
  AND i_2021.value IS NULL; -- Memeriksa apakah data untuk tahun yang diinginkan sudah ada
-- 2022 copy dari 2021
INSERT INTO isi (instansi, indikator, year, value)
SELECT 
    i_2021.instansi,
    i_2021.indikator,
    2022 AS year,  -- Tahun yang ingin Anda sisipkan jika data tahun sebelumnya tidak ada
    COALESCE(i_2022.value, i_2021.value) AS value  -- Mengambil nilai dari tahun sebelumnya jika data tidak ada untuk tahun yang diinginkan
FROM isi i_2021
LEFT JOIN isi i_2022 ON i_2021.instansi = i_2022.instansi AND i_2021.indikator = i_2022.indikator AND i_2022.year = 2022
WHERE i_2021.year = 2021
  AND i_2022.value IS NULL; -- Memeriksa apakah data untuk tahun yang diinginkan sudah ada
-- 2023 copy dari 2022
INSERT INTO isi (instansi, indikator, year, value)
SELECT 
    i_2022.instansi,
    i_2022.indikator,
    2023 AS year,  -- Tahun yang ingin Anda sisipkan jika data tahun sebelumnya tidak ada
    COALESCE(i_2023.value, i_2022.value) AS value  -- Mengambil nilai dari tahun sebelumnya jika data tidak ada untuk tahun yang diinginkan
FROM isi i_2022
LEFT JOIN isi i_2023 ON i_2022.instansi = i_2023.instansi AND i_2022.indikator = i_2023.indikator AND i_2023.year = 2023
WHERE i_2022.year = 2022
  AND i_2023.value IS NULL; -- Memeriksa apakah data untuk tahun yang diinginkan sudah ada