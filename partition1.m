function [array pp] = partition1(array)
% use the first element as pivot

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



