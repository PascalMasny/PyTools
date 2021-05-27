function [null] = asdf(filepath, visual) #get data from Python


data=csvread(filepath); % read csv file

x=data(:,3); % read 3rd column
y=data(:,2); % read 2nd cloumn

plot(x,y) %plot data

saveas(gcf,'curve.png') #safe plot as a picture


endfunction
