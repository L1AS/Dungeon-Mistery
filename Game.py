import random
#进入地下城，
#可以随机抽取武器 (rouge-like)

Weapon_list = {
  "default":["攻击","基础成功概率","主属性","额外效果"],
  "剑":[5,50%,"力量",""]
}

#每一点主属性+1%的成功率，每一点主属性+1的攻击力，最高90%\

def start():
  global weapon
  weapon = "空手"
  print("你来到了地下室，你前面有一扇门……")
#文本缺失
  randomizer()

  
#随机出现房间，1.战斗50%，2.宝箱30%，3.回血19%，4.抽奖1%
#抽奖：1.+5点主属性50%，3.+10点主属性40%，2.死亡10%
def randomizer():
  x = random.randint(0,99)
  if x >= 50:
    fight()
  elif x < 50 and x >=20:
    chest()
  elif x <20 and x>=1:
    heal()
  else:
    Lucky_draw()
