# IN628 2019 Practical 14.1 - Intro to Ruby

=begin
Your assignment program must be written in "idiomatic Ruby". Before you can begin implementing 
it, therefore, you will need to study Ruby. While you don't need to be (and cannot reasonably 
be expected to become in the next three weeks) a Ruby expert, you will need to understand core 
Ruby features, especially those that are substantively different from the traditional imperative 
languages that you have used before. 

This lab provides a checklist of language features you should know, questions you should be able 
to answer, and code examples you should understand before beginning to design and implement your assignment. 
Not all of the specific elements described here will be required in your implementation, nor is everything you 
need to know listed here. However, when you can complete the checklist, you will have done enough preparation 
to be able to begin.
=end

=begin
1.	Explain fully each of these Ruby language features/elements:

    a.	blocks
    b.  iterators
    c.  interpolation
    d.  yield
    e.  unless
    f.  .inspect
    g.  .times
    h.  .each
    i.  .collect
    j.  .split, .scan, .squeeze, .chomp, etc.
    k.  .dup
    l.  .count
    m.  .all?
    n.  .include?
    o.  %w
    p.  attr_reader & attr_writer
    q.  @var_name and @@var_name
    r.  $stdout.flush
    s.  print vs. puts
    t.  nil
=end

=begin
2.  Answer these questions fully:

    a.  Why do people say that "Ruby is a pure OO language", as opposed to Java, C++, etc., 
        which are not considered "pure OO"?
    
    b.  What is the syntax for method calls with 0 arguments?

    c.  What are the rules about use of the return keyword in functions that return a result?

    d.  What does it mean if a function has '!',  '?', or  '=' on the end of its name?

    e.  How do you read from a text file?

    f.  How do you populate an array from a text file (each line as an element in the array)?

    g.  How do you randomly select an element from an array using idiomatic Ruby?

    h.  How can you add elements to an array (increasing the size of the array) using idiomatic Ruby?

    i.  How can you get user input from stdin?

    j. How do you iterate over the individual characters in a string using idiomatic Ruby?

=end

# 3.  Explain what each of these code samples will do:  

'abc'.length.times do
	print "bob\t"
end

# a.  Write your explaination here

(0..11).each_slice(3) { |n1, n2, n3| puts n1 + n2 + n3}

# b.  Write your explaination here

puts (10..20).collect {|num| num * num}.join('..')

# c.  Write your explaination here

%w{Amsterdam Berlin Paris}.reverse_each do |city|
	puts city.reverse
end

# d.  Write your explaination here

letters = 'a'..'h'
double_letters = letters.each.collect {|d| d.succ}
puts double_letters.inspect
double_letters.each {|db| puts db.upcase}

# e.  Write your explaination here 

def yield_three_times_with_arg(arg)
	yield arg
	yield arg
	yield arg
end
yield_three_times_with_arg('bob') {|arg| print arg.upcase}
yield_three_times_with_arg('bob') {|arg| print arg.capitalize}

# f.  Write your explaination here 

def mystery_method(input_str)
	input_str.split('').all? {|c| input_str.count(c) == 2}
end

puts mystery_method('hannah')
puts mystery_method('banana')

# g.  Write your explaination here 