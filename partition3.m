function [array pp] = partition3(array)
% use the median element as pivot
% first exchange pivot with the first element

n = length(array);
first = array(1);
last = array(end);
if mod(n,2) == 0
    middle_p = n/2;
else
    middle_p = floor(n/2)+1;
end

middle = array(middle_p);

mm = median([first middle last]); % median value

if mm == first
    mm_p = 1;
elseif mm == middle
    mm_p = middle_p;
else
    mm_p = n;
end


temp = array(mm_p);
array(mm_p) = array(1);
array(1) = temp;


pivot = array(1);

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



