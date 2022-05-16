clear
clc
Y0 = [ 1 ; 0 ] ;
[t1 y1] = ode23( @solver, [0 15] ,Y0 );
[t2 y2] = ode45( @solver, [0 15] ,Y0 );
subplot(2,3,1)
plot(t1,y1(:,1))
axis([0 15 -0.5 1])
legend('y1')
title('ode23')
grid on
subplot(2,3,2)
plot(t2,y2(:,1))
axis([0 15 -0.5 1])
grid on
legend('y1')
title('ode45')
c1=87/85;
c2=26/85;
f=@(t)exp(-t)*(c1*cos(3*t)+c2*sin(3*t))+1/85*(9*sin(t)-2*cos(t));
df=@(t)exp(-t)*(-3*c1*sin(3*t)+3*c2*cos(3*t))-exp(-t)*(c1*cos(3*t)+c2*sin(3*t))+1/85*(9*cos(t)+2*sin(t));
subplot(2,3,3)
fplot(f,[0 15])
grid on
legend('y1')
title('solve')

subplot(2,3,4)
plot(t1,y1(:,2))
axis([0 15 -3 1])
legend('y2')
title('ode23')
grid on
subplot(2,3,5)
plot(t2,y2(:,2))
axis([0 15 -3 1])
legend('y2')
title('ode45')
grid on

subplot(2,3,6)
fplot(df,[0 15])
legend('y2')
title('solve')
grid on