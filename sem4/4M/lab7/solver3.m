function [ dydt ] = solver3( t,Y0 )

dydt=[Y0(2) ; -1/t^2 ] ;
end