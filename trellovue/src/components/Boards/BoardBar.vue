<template>
  <navbar class="" style="display:flex; align-items: center; max-height: 60px">

    <div class="navbar__title">
      <span class="title">{{ title }}</span>
    </div>

    <div class="navbar__icon">
      <svg class="icon" id="" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
           viewBox="0 0 270.365 270.365" xml:space="preserve">
          <path style="" d="M269.884,103.996c-0.943-2.903-4.038-7.772-14.162-7.772h-73.543c-4.999,0-10.958-4.329-12.503-9.083
	l-22.726-69.945c-3.129-9.628-8.717-11.065-11.769-11.065c-3.052,0-8.64,1.438-11.769,11.066l-22.726,69.944
	c-1.545,4.754-7.504,9.083-12.502,9.083H14.642c-10.125,0-13.219,4.869-14.162,7.772c-0.943,2.902-1.302,8.661,6.89,14.612
	l59.497,43.226c4.044,2.939,6.32,9.944,4.775,14.698l-22.726,69.943c-1.867,5.745-1.578,10.358,0.858,13.711
	c1.868,2.572,4.827,4.047,8.118,4.047c3.14-0.001,6.432-1.283,10.065-3.923l59.497-43.227c1.929-1.401,4.745-2.205,7.729-2.205
	c2.982,0,5.798,0.804,7.727,2.205l59.497,43.229c3.634,2.639,6.927,3.922,10.066,3.922c3.29-0.001,6.248-1.476,8.116-4.048
	c2.437-3.352,2.725-7.966,0.858-13.709l-22.726-69.945c-1.545-4.753,0.731-11.759,4.775-14.697l59.499-43.226
	C271.187,112.656,270.828,106.899,269.884,103.996z M194.681,149.7c-9.277,6.74-13.769,20.563-10.225,31.468l20.228,62.258
	l-52.958-38.478c-4.499-3.27-10.374-5.069-16.543-5.069c-6.169,0-12.045,1.8-16.545,5.069L65.68,243.426l20.228-62.257
	c3.544-10.906-0.947-24.729-10.225-31.469l-52.959-38.477h65.462c11.466,0,23.224-8.543,26.767-19.448l20.229-62.259l20.229,62.259
	c3.544,10.905,15.302,19.448,26.769,19.448h65.462L194.681,149.7z"/>
</svg>
    </div>

    <hr class="line">

    <div class="navbar__item">
      <img class="icon" src="@/static/images/Boards/Body/profile.svg"  alt="">
      <span style="margin-left: 5px">Для рабочего пространства</span>
    </div>

    <hr class="line">

    <div class="navbar__item" >
      <img class="icon" src="@/static/images/Boards/Body/filter.svg"  alt="">
      <span style="margin-left: 5px">Фильтр</span>
    </div>

    <hr class="line">

    <div class="profile-icon">
      <span>{{ username }}</span>
    </div>

    <hr class="line">

    <div class="navbar__item" style="padding: 5px 8px 7px 6px">
      <span style="margin-left: 5px">. . . </span>
    </div>



    <hr class="line">

    <div class="navbar__item" style="background-color: white">
      <img class="icon" src="@/static/images/Boards/Body/add-user.svg"  alt="">
      <span style="margin-left: 5px; color: black"> Поделиться</span>
    </div>

  </navbar>
</template>

<script>
import Cookies from "js-cookie";
export default {
  props: {
    title: String,
  },
  data() {
    return {
      username: null,
    }

  },
  methods:{
    get_username(){
      this.username = Cookies.get('username')
      this.username = this.username.substring(0,1)
    }
  },
  mounted() {
    this.get_username()
  }
}
</script>

<style scoped>



.icon {
  width: 20px;
  margin:  auto;
  fill: white;
  z-index: 20;
  cursor: pointer;
}




navbar{
  padding: 20px;
}

.navbar__title{
  padding: 5px 15px 5px 15px;
  margin-right: 5px;
  height: 100%;
  border-radius: 4px;
  transition: background-color 150ms;
  cursor: pointer;
}

.navbar__title:hover{
  background-color: rgba(241, 237, 237, 0.27);
}

.title{
  font-size: 18px;
  color: white;
  font-weight: 700;
}


.navbar__icon{
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 5px;
  height: 36px;
  width: 36px;
  border-radius: 4px;
  transition: fill, width 150ms;
  background-color: rgba(241, 237, 237, 0.27);
  cursor: pointer;
}

.navbar__icon:hover .icon{
  width: 22px;
  fill: yellow;
}

.line{
  height: 26px;
  width: 1px;
  margin-right: 5px;
  color: #ffffff;
  transform: rotate(200grad);
}

.navbar__item{
  margin-right: 5px;
  padding: 6.5px;
  background-color: rgba(241, 237, 237, 0.27);
  border-radius: 4px;
  color: white;
  transition: background-color 150ms;
  cursor: pointer;
}

.navbar__item:hover{
  background-color: rgba(241, 237, 237, 0.55);
}


.profile-icon{
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 18px;
  border-radius: 100%;
  margin-right: 5px;
  background-color: #0c50c9;
  transition: background-color 150ms;
  cursor: pointer ;
}

.profile-icon:hover{
  background-color: #3574e3;

}

</style>