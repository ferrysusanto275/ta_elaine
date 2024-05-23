SELECT i_2018.instansi,
i_2018.indikator,i_2018.value '2018',
i_2019.value '2019',
i_2020.value '2020',
i_2021.value '2021',
i_2022.value '2022',
i_2023.value '2023' 
FROM isi i_2018
left JOIN isi i_2019 ON i_2018.instansi=i_2019.instansi AND i_2018.indikator=i_2019.indikator AND i_2019.`year`=2019
left JOIN isi i_2020 ON i_2018.instansi=i_2020.instansi AND i_2018.indikator=i_2020.indikator AND i_2020.`year`=2020
left JOIN isi i_2021 ON i_2018.instansi=i_2021.instansi AND i_2018.indikator=i_2021.indikator AND i_2021.`year`=2021
left JOIN isi i_2022 ON i_2018.instansi=i_2022.instansi AND i_2018.indikator=i_2022.indikator AND i_2022.`year`=2022
left JOIN isi i_2023 ON i_2018.instansi=i_2023.instansi AND i_2018.indikator=i_2023.indikator AND i_2023.`year`=2023
WHERE i_2018.YEAR=2018
AND (i_2019.value IS NULL
OR i_2020.value IS NULL
OR i_2021.value IS NULL
OR i_2022.value IS NULL
OR i_2023.value IS NULL
)
