%dfs_loop_two

function following = dfs_loop_two(graph,n,fntym)

global  explored following leader

% ftcnt = 0; % finishing time count
% fntym = zeros(n,1); % finishing time of each node
explored = zeros(n,1); % indicator of whether a node has been explored or not
following = zeros(n,1); % indicate which leader it follows, could be itself


for j = n:-1:1
    i = find(fntym==j);
    if ~explored(i)
        leader = i;
        dfs_two(graph,i);
    end
end

