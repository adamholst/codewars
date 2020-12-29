select generate_series as numbers, 
  case when generate_series % 15 = 0
    then 'fizzbuzz' 
  when generate_series % 3 = 0 
    then 'fizz' 
  when generate_series % 5 = 0 
    then 'buzz' 
  else ''
  end as "fizzbuzz numbers"
  
from generate_series(1, 100);
