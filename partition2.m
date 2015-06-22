function [array pp] = partition2(array)
% use the last element as pivot
% first exchange pivot with the first element

temp = array(end);
array(end) = array(1);
array(1) = temp;


pivot = array(1);
n = length(array);
i = 2; % pointer for left part

for j = 2:n
    if array(j) < pivot
        tmp = array(i);
        array(i) = array(j);
        array(j) = tmp;
        i = i + 1;
    end
end
array(1) = array(i-1);
array(i-1) = pivot;
pp = i - 1; % i-1 is the position of pivot



