SELECT *,
round((i1*bobot_i1+i2*bobot_i2+i3*bobot_i3+i4*bobot_i4+i5*bobot_i5+i6*bobot_i6+i7*bobot_i7+i8*bobot_i8+i9*bobot_i9+i10*bobot_i10) / bobot_aspek1,2) AS `aspek1`,
round((i11*bobot_i11+i12*bobot_i12+i13*bobot_i13+i14*bobot_i14)/bobot_aspek2,2) AS `aspek2`,
round((i15*bobot_i15+i16*bobot_i16+i17*bobot_i17+i18*bobot_i18)/bobot_aspek3,2) AS `aspek3`,
round((i19*bobot_i19+i20*bobot_i20) / bobot_aspek4,2) AS `aspek4`,
round((i21*bobot_i21+i22*bobot_i22+i23*bobot_i23+i24*bobot_i24+i25*bobot_i25+i26*bobot_i26+i27*bobot_i27+i28*bobot_i28)/ bobot_aspek5,2) AS `aspek5`,
round((i29*bobot_i29+i30*bobot_i30+i31*bobot_i31) / bobot_aspek6,2) AS `aspek6`,
round((i32*bobot_i32+i33*bobot_i33+i34*bobot_i34+i35*bobot_i35+i36*bobot_i36+i37*bobot_i37+i38*bobot_i38+i39*bobot_i39+i40*bobot_i40+i41*bobot_i41 )/ bobot_aspek7,2) AS `aspek7`,
round((i42*bobot_i42+i43*bobot_i43+i44*bobot_i44+i45*bobot_i45+i46*bobot_i46+i47*bobot_i47 )/ bobot_aspek8,2) AS `aspek8`
from all_isi

SELECT *, 
ROUND((aspek1*bobot_aspek1)/bobot_domain1,2) AS 'domain1',
ROUND((aspek2*bobot_aspek2 +aspek3*bobot_aspek3+aspek4*bobot_aspek4)/bobot_doamin2, 2 ) AS 'domain2',
ROUND((aspek5*bobot_aspek5 + aspek6*bobot_aspek6)/bobot_domain3,2) AS 'domain3' ,
ROUND((aspek7*bobot_aspek7 + aspek8*bobot_aspek8)/bobot_domain4,1)AS 'domain4', 
