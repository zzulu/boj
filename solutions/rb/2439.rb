n = gets.chomp.to_i
1.upto(n).each {|i| puts "#{"\s"*(n-i)}#{"*"*i}"}
