select `i`.`id` AS `id`,`i`.`nama` AS `nama`,
`gi`.`id` AS `gi_id`,`gi`.`nama` AS `gi_nama`,
`tp`.`id` AS `tp_id`,`tp`.`nama` AS `tp_nama`,tp.x,tp.y,
`m`.`year` AS `year`,
`m`.`value` AS `i1`,
(select bobot from indikator where id='in2023110400001') as'bobot_i1',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400002' and `year` = `m`.`year`) AS `i2`,
(select bobot from indikator where id='in2023110400002') as'bobot_i2',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400003' and `year` = `m`.`year`) AS `i3`,
(select bobot from indikator where id='in2023110400003') as'bobot_i3',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400004' and `year` = `m`.`year`) AS `i4`,
(select bobot from indikator where id='in2023110400004') as'bobot_i4',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400005' and `year` = `m`.`year`) AS `i5`,
(select bobot from indikator where id='in2023110400005') as'bobot_i5',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400006' and `year` = `m`.`year`) AS `i6`,
(select bobot from indikator where id='in2023110400006') as'bobot_i6',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400007' and `year` = `m`.`year`) AS `i7`,
(select bobot from indikator where id='in2023110400007') as'bobot_i7',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400008' and `year` = `m`.`year`) AS `i8`,
(select bobot from indikator where id='in2023110400008') as'bobot_i8',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400009' and `year` = `m`.`year`) AS `i9`,
(select bobot from indikator where id='in2023110400009') as'bobot_i9',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400010' and `year` = `m`.`year`) AS `i10`,
(select bobot from indikator where id='in2023110400010') as'bobot_i10',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400011' and `year` = `m`.`year`) AS `i11`,
(select bobot from indikator where id='in2023110400011') as'bobot_i11',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400012' and `year` = `m`.`year`) AS `i12`,
(select bobot from indikator where id='in2023110400012') as'bobot_i12',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400013' and `year` = `m`.`year`) AS `i13`,
(select bobot from indikator where id='in2023110400013') as'bobot_i13',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400014' and `year` = `m`.`year`) AS `i14`,
(select bobot from indikator where id='in2023110400014') as'bobot_i14',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400015' and `year` = `m`.`year`) AS `i15`,
(select bobot from indikator where id='in2023110400015') as'bobot_i15',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400016' and `year` = `m`.`year`) AS `i16`,
(select bobot from indikator where id='in2023110400016') as'bobot_i16',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400017' and `year` = `m`.`year`) AS `i17`,
(select bobot from indikator where id='in2023110400017') as'bobot_i17',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400018' and `year` = `m`.`year`) AS `i18`,
(select bobot from indikator where id='in2023110400018') as'bobot_i18',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400019' and `year` = `m`.`year`) AS `i19`,
(select bobot from indikator where id='in2023110400019') as'bobot_i19',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400020' and `year` = `m`.`year`) AS `i20`,
(select bobot from indikator where id='in2023110400020') as'bobot_i20',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400021' and `year` = `m`.`year`) AS `i21`,
(select bobot from indikator where id='in2023110400021') as'bobot_i21',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400022' and `year` = `m`.`year`) AS `i22`,
(select bobot from indikator where id='in2023110400022') as'bobot_i22',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400023' and `year` = `m`.`year`) AS `i23`,
(select bobot from indikator where id='in2023110400023') as'bobot_i23',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400024' and `year` = `m`.`year`) AS `i24`,
(select bobot from indikator where id='in2023110400024') as'bobot_i24',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400025' and `year` = `m`.`year`) AS `i25`,
(select bobot from indikator where id='in2023110400025') as'bobot_i25',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400026' and `year` = `m`.`year`) AS `i26`,
(select bobot from indikator where id='in2023110400026') as'bobot_i26',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400027' and `year` = `m`.`year`) AS `i27`,
(select bobot from indikator where id='in2023110400027') as'bobot_i27',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400028' and `year` = `m`.`year`) AS `i28`,
(select bobot from indikator where id='in2023110400028') as'bobot_i28',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400029' and `year` = `m`.`year`) AS `i29`,
(select bobot from indikator where id='in2023110400029') as'bobot_i29',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400030' and `year` = `m`.`year`) AS `i30`,
(select bobot from indikator where id='in2023110400030') as'bobot_i30',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400031' and `year` = `m`.`year`) AS `i31`,
(select bobot from indikator where id='in2023110400031') as'bobot_i31',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400032' and `year` = `m`.`year`) AS `i32`,
(select bobot from indikator where id='in2023110400032') as'bobot_i32',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400033' and `year` = `m`.`year`) AS `i33`,
(select bobot from indikator where id='in2023110400033') as'bobot_i33',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400034' and `year` = `m`.`year`) AS `i34`,
(select bobot from indikator where id='in2023110400034') as'bobot_i34',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400035' and `year` = `m`.`year`) AS `i35`,
(select bobot from indikator where id='in2023110400035') as'bobot_i35',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400036' and `year` = `m`.`year`) AS `i36`,
(select bobot from indikator where id='in2023110400036') as'bobot_i36',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400037' and `year` = `m`.`year`) AS `i37`,
(select bobot from indikator where id='in2023110400037') as'bobot_i37',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400038' and `year` = `m`.`year`) AS `i38`,
(select bobot from indikator where id='in2023110400038') as'bobot_i38',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400039' and `year` = `m`.`year`) AS `i39`,
(select bobot from indikator where id='in2023110400039') as'bobot_i39',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400040' and `year` = `m`.`year`) AS `i40`,
(select bobot from indikator where id='in2023110400040') as'bobot_i40',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400041' and `year` = `m`.`year`) AS `i41`,
(select bobot from indikator where id='in2023110400041') as'bobot_i41',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400042' and `year` = `m`.`year`) AS `i42`,
(select bobot from indikator where id='in2023110400042') as'bobot_i42',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400043' and `year` = `m`.`year`) AS `i43`,
(select bobot from indikator where id='in2023110400043') as'bobot_i43',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400044' and `year` = `m`.`year`) AS `i44`,
(select bobot from indikator where id='in2023110400044') as'bobot_i44',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400045' and `year` = `m`.`year`) AS `i45`,
(select bobot from indikator where id='in2023110400045') as'bobot_i45',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400046' and `year` = `m`.`year`) AS `i46`,
(select bobot from indikator where id='in2023110400046') as'bobot_i46',
(select value from `isi`  where instansi = `i`.`id` and indikator = 'in2023110400047' and `year` = `m`.`year`) AS `i47`,
(select bobot from indikator where id='in2023110400047') as'bobot_i47',
(select bobot from aspek where id='a2023110400001') as'bobot_aspek1',
(select bobot from aspek where id='a2023110400002') as'bobot_aspek2',
(select bobot from aspek where id='a2023110400003') as'bobot_aspek3',
(select bobot from aspek where id='a2023110400004') as'bobot_aspek4',
(select bobot from aspek where id='a2023110400005') as'bobot_aspek5',
(select bobot from aspek where id='a2023110400006') as'bobot_aspek6',
(select bobot from aspek where id='a2023110400007') as'bobot_aspek7',
(select bobot from aspek where id='a2023110400008') as'bobot_aspek8',
(select bobot from domain where id='d2023110400001') as'bobot_domain1',
(select bobot from domain where id='d2023110400002') as'bobot_domain2',
(select bobot from domain where id='d2023110400003') as'bobot_domain3',
(select bobot from domain where id='d2023110400004') as'bobot_domain4'
from instansi `i` 
join `isi` `m` on`m`.`instansi` = `i`.`id` and `m`.`indikator` = 'in2023110400001' 
join `grup_instansi` `gi` on`i`.`group_instansi` = `gi`.`id`
left JOIN titik_peta tp ON gi.titik_peta=tp.id