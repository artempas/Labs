function [ dydt ] = solver( t,Y0 )
dydt=[Y0(2) ; -2*Y0(2)-10*Y0(1)+ sin(t) ] ;
end