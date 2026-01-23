# python3 -m venv ~/Documents/.venv
# source ~/Documents/.venv/bin/activate
source .venv/bin/activate

python3 _cmd.py schema
python3 _cmd.py db -db -all
python3 _cmd.py db -table -all
python3 _cmd.py db -seed -all

python3 _cmd.py java -all

python3 _cmd.py admin -all

# python3 _cmd.py uni page -all
# python3 _cmd.py -all

# python3 _cmd.py db -sql