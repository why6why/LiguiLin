import request from '@/utils/request'

export default{
  getUserList(searchModel){
    return request({
      url: '/user/list',
      method: 'get',
      params:{
        pageNo: searchModel.pageNo,
        pageSize: searchModel.pageSize,
        username: searchModel.username,
        phone: searchModel.phone
      }
    });
  },
 async bigModel(searchModel){
    console.log("why data")
    console.log(searchModel)
    const res = await request({
      url: '/v1/chat/completions',
      method: 'post',
      data: {
        "model": "cele/Cele-72B-Chat-GPTQ-Int4",
        "messages": [
            {
                "role": "system",
                "content": "你是一个商品类目预测专家，对输入的内容，进行商品类目预测，类目包含'大家电、全屋家具、营养保健、茶饮冲调、休闲零食、生鲜水果、肉禽蛋品、粮油调味、中外名酒、家居用品、当地玩乐、旅游酒店、智能锁、华帝电器专场、生活电器、厨房电器、空调'。返回商品的分类。如果返回的类目不在包含的内容中，返回'明星单品'四字"
            },
            {
                "role": "user",
                "content": "金龙鱼"
            }
        ],
        "temperature": 0.1
    }
    });
    console.log(res);
    
  },
  addUser(user){
    return request({
      url: '/user',
      method: 'post',
      data: user
    });
  },
  updateUser(user){
    return request({
      url: '/user',
      method: 'put',
      data: user
    });
  },
  saveUser(user){
    if(user.id == null && user.id == undefined){
      return this.addUser(user);
    }
    return this.updateUser(user);
  },
  getUserById(id){
    return request({
      //url: '/user/' + id,
      url: `/user/${id}`,
      method: 'get'
    });
  },
  deleteUserById(id){
    return request({
      url: `/user/${id}`,
      method: 'delete'
    });
  },
}