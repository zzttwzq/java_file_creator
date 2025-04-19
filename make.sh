# 创建名为 myenv 的虚拟环境
# python3 -m venv myenv      
# source ./myenv/bin/activate
# python3 _cmd.py db -sql '';

python3 _cmd.py schema
python3 _cmd.py db -db -all
python3 _cmd.py db -table -all
python3 _cmd.py db -seed -all

python3 _cmd.py java -all
# python3 _cmd.py java model,mapper,provider,service,controller user
# python3 _cmd.py java model user
# python3 _cmd.py java mapper user
# python3 _cmd.py java provider user
# python3 _cmd.py java service user
# python3 _cmd.py java controller user
# python3 _cmd.py java -d user

python3 _cmd.py admin -all

# python3 _cmd.py uni page -all
# python3 _cmd.py -all
