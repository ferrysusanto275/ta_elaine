-- isi 2021 sama data 2022
INSERT INTO `isi` (`instansi`, `indikator`, `value`, `year`)
SELECT m.instansi, m.indikator, m.value, '2021' AS 'year'
FROM `isi` m
WHERE m.year = 2022
AND m.indikator NOT IN (
    SELECT o.indikator FROM `isi` o WHERE o.year = 2021 AND o.instansi = m.instansi
);
-- isi 2022 sama data 2021
INSERT INTO `isi` (`instansi`, `indikator`, `value`, `year`)
SELECT m.instansi, m.indikator, m.value, '2022' AS 'year'
FROM `isi` m
WHERE m.year = 2021
AND m.indikator NOT IN (
    SELECT o.indikator FROM `isi` o WHERE o.year = 2022 AND o.instansi = m.instansi
);