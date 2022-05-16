clear
clc
hold on
grid on
Y0 = [ log(0.01) ; 1/0.01 ] ;
[t y] = ode45( @solver3, [0.01 1] ,Y0 );
plot(t,y(:,1))
fplot(@(t) log(t),[0.01 1],'r')
xlabel('t')
ylabel('y')
legend('ode45','log(t)')
title('d2y=-1/t^2, y(0.01)=ln(0.01)')