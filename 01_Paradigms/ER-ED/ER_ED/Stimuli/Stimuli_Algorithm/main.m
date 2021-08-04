% obj_fx - contains the calculation of the objective function -> how good
% is the fit of the current categorization 
% ga_fx - the genetic algorithm

%% load data

data = load('negative.mat');
data = data.negative;

%% define fitting values

D.clusters = 5; % how many clusters
D.data = data;

D.n_init = 30; % the number of individuals of the initial population
D.n_new  = 6*D.n_init; % 5 to 7 times the inital population (for comma-selection)
D.sig = 1; % sigma -> how many items are changed for one mutation 
D.iterations = 1000; % maximum number of iterations

% define the objective function 
D.ObjFun = @(x, d)obj_fx(x, d);

%% execute GA

[P, best] = ga_fx(D);

%% show best solution

best = P(best).A(1).G

for i=1:D.clusters
    mean(data(best==i, :))
end




