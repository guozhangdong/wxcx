import { request } from '../../utils/request';
Page({
  onLoad(o) { this.orderId = o.orderId; this.openid = wx.getStorageSync('openid'); this.pay(); },
  async pay() {
    const p = await request({ url:'/api/v1/payment/create', method:'POST', data:{ orderId:this.orderId, openid:this.openid }});
    wx.requestPayment({ timeStamp:p.timeStamp, nonceStr:p.nonceStr, package:p.package, signType:p.signType, paySign:p.paySign });
  }
});
