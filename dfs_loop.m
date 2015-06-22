% DFS-Loop

function [following fntym] = dfs_loop(graph,n)

global ftcnt fntym explored following leader

ftcnt = 0; % finishing time count
fntym = zeros(n,1); % finishing time of each node
explored = zeros(n,1); % indicator of whether a node has been explored or not
following = zeros(n,1); % indicate which leader it follows, could be itself


for i = n:-1:1
    if ~explored(i)
        leader = i;
        dfs(graph,i);
    end
end
    

