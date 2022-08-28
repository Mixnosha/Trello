<template>
  <div class="right__navbar">
    <div class="right__lbl" style="">
      <div class="lbl">
        <img src="@/static/images/square-board.svg" style="width: 14px;">
        <div style="padding-left: 10px">Доски</div>
      </div>
      <div class="lbl">
        <img src="@/static/images/main.svg" style="width: 14px;">
        <div style="padding-left: 10px">Главная страница</div>

      </div>
    </div>
    <div class="right_workspaces">
      <div>
        <div class="add__workspaces">
          <div class="add__lbl" style="padding-right:90px; display: flex; align-items: center; justify-content: center">
            Рабочие пространства
          </div>
          <div class="add"
               style="border-radius: 5px;padding-right:10px; padding-left: 10px; font-weight: normal;color: #596477; font-size: 24px; display: flex; align-items: center; justify-content: center"
               @click="new_wk=true">
            +
          </div>
        </div>
        <div v-for="wk in workspaces">
          <div class="workspace" :id="'workspace'+wk.id" @click="menuVisible(wk.id)">
            <div class="workspace__icon" style="display: flex; align-items: center; justify-content: center">
              <img :src="wk.logo" style="width: 20px; border-radius: 4px">
            </div>
            <div class="workspace__title"
                 style="padding-left:5px; width: 100%">{{ wk.title }}
            </div>
          </div>
          <div :id='"open__menu"+wk.id' style="display: none">
            <div class="open__menu-label">
              <img src="@/static/images/square-board.svg" alt="" width="12px">
              <div class="open__lbl">Доски</div>
            </div>
            <div class="open__menu-label">
              <img src="@/static/images/heart.svg" width="12px" alt="">
              <div class="open__lbl">Важнейшие события</div>
            </div>
            <div class="open__menu-label">
              <img src="@/static/images/menu.svg" width="12px" alt="">
              <div class="open__lbl">Представления</div>
            </div>
            <div class="open__menu-label">
              <img src="@/static/images/networking.svg" width="12px" alt="">
              <div class="open__lbl">Участники</div>
            </div>
            <div class="open__menu-label">
              <img src="@/static/images/settings.svg" width="12px" alt="">
              <div class="open__lbl">Найстройки</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="new__wk-back" :style="newWk()">
    <div class="new__wk">
      <div class="form__wk" style="width: 50%; height: 100%; padding: 76px">
        <div class="new__wk-label" style="padding-bottom: 20px">
          <div style="font-size: 24px; font-weight: 700; padding-bottom: 8px">Создайте рабочее пространство</div>
          <div style="font-size: 18px; color: gray">Повысьте производительность: участники команды смогут получать
            удобный доступ ко всем доскам.
          </div>
        </div>

        <div class="new__wk-form">
          <div class="form-title" style="padding-bottom: 32px">
            <div style="font-size: 12px; font-weight: 700; padding-bottom: 4px">Название рабочего пространства</div>
            <div style="padding-bottom: 4px"><input v-model="newWkForm.title"
                                                    style="width: 100%; height: 48px; border-radius: 2px; border: 2px solid rgba(128,128,128,0.47)"
                                                    type="text" placeholder="Компания <<Тако>>"></div>
            <div style="font-size: 12px; color: gray">Укажите название вашей команды, компании или организации.</div>
          </div>
          <div class="form-title" style="padding-bottom: 32px">
            <div style="font-size: 12px; font-weight: 700; padding-bottom: 4px">Тип рабочего пространства</div>
            <div style="color: gray">
              <select v-model="newWkForm.status"
                      style="background: white; border-radius: 4px; border: 2px solid rgba(128,128,128,0.47); width: 100%; height: 42px; color: rgba(0,0,0,0.72); font-size: 16px; padding-left: 12px">
                <option style="height: 20px" value="">Выбрать...</option>
                <option value=3>Операции</option>
                <option value=2>Образование</option>
                <option value=4>Продажи CRM</option>
                <option value=1>Малый бизнес</option>
                <option value=2>Управление Персоналом</option>
                <option value=5>Маркейтинг</option>
                <option value=6>Инженерия IT</option>
                <option value=7>Образование</option>
                <option value=8>Другое</option>
              </select></div>
          </div>

          <div class="form-title" style="padding-bottom: 24px">
            <div class="" style="display:flex; align-items: center;">
              <div style="font-size: 12px; font-weight: 700; padding-bottom: 4px; padding-right: 2px">Описание рабочего
                пространства
              </div>
              <div class="" style="color: rgba(128,128,128,0.67); font-size: 12px">Необязательно</div>
            </div>
            <textarea v-model="newWkForm.description"
                      style="resize: none; padding: 10px; width: 100%; height: 120px;border-radius: 2px; border: 2px solid rgba(128,128,128,0.47); font-size: 15px"
                      placeholder="Здесь наша команда хранит всю нужную информацию."></textarea>
            <div style="font-size: 12px; color: gray">Расскажите участникам немного о рабочем пространстве.</div>
          </div>
          <div>
            <button @click="sendWkForm"
                style="width: 100%; height: 48px; background: #0265f8; border: none; color: white; border-radius: 4px">
              Продолжить
            </button>
          </div>
        </div>
      </div>
      <div class="image__wk" style="width: 50%; height: 100%">
        <div style="display: flex; align-items: center; padding-top: 20px;">
          <div style="padding-right: 94%"></div>
          <div @click="new_wk=false" class="close__wk-cr"
               style="transform: rotate(45deg);color: #42526e; font-size: 32px; cursor: pointer">+
          </div>
        </div>
        <img src="@/static/images/empty_board.svg" style="padding-top: 80px; padding-left: 90px;">
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
import up_arrow from '@/static/images/up-arrow.svg'
import right_arrow from '@/static/images/arrow_right.svg'
import {mapMutations, mapState} from "vuex";

export default {
  data() {
    return {
      menu_visible: false,
      new_wk: false,
      newWkForm: {
        title: '',
        status: '',
        description: '',
      }
    }
  },
  methods: {
    ...mapMutations({
      setWorkspaces: 'navbar/setWorkspaces',
    }),
    newWk() {
      if (this.new_wk === false) {
        return {display: 'none'}
      } else {
        return {new_wk: 'flex'}
      }
    },
    loadWK() {
      axios.get('http://192.168.100.6:8000/api/v1/workspace/', {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        this.setWorkspaces(res.data)
      })
    },
    sendWkForm() {
      axios.post('http://192.168.100.6:8000/api/v1/workspace/', {
        title: this.newWkForm.title,
        status: 1,
        type: Number(this.newWkForm.status),
      }, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        console.log(res.status)
        if (res.status === 201){
          this.$router.push({ name: 'pageWk', params: { slug: 'tako123' }})
        }
        else {
          console.log('произошла внутрення ошибка сервера')}
      })
    },
    menuVisible(el) {
      const id = "open__menu" + el
      const men_id = "workspace" + el
      let menu = document.getElementById(id)
      if (menu.style.display === 'none') {
        menu.style.display = 'block'
        document.getElementById(men_id).style.background = `rgba(150, 180, 231, 0.32) url(${up_arrow}) no-repeat 95% 50%`
        document.getElementById(men_id).style.backgroundSize = "12px"
      } else {
        menu.style.display = 'none'
        document.getElementById(men_id).style.background = ''
        document.getElementById(men_id).style.backgroundSize = "12px"
      }
    },
  },
  watch: {},
  mounted() {
    this.loadWK()
  },
  computed: {
    ...mapState({
      workspaces: state => state.navbar.workspaces,
    }),
  }
}
</script>

<style scoped>

.right__navbar {
  width: 258px;
  padding: 40px 0px;
  margin-left: 86px;

}

.lbl {
  font-weight: 700;
  display: flex;
  align-items: center;
  font-size: 15px;
  padding: 5px 0px 5px 5px;
  transition: background-color 64ms;
  border-radius: 3px;
  color: #293342;
}

.lbl:hover {
  background: rgba(150, 180, 231, 0.32);
}

.add__workspaces {
  display: flex;
  font-size: 12px;
  font-weight: 700;
  color: #42526e;
  padding: 10px 0px 4px 0px;
}

.workspace {
  width: 100%;
  display: flex;
  align-items: center;
  padding: 10px;
  margin-bottom: 8px;
  border-radius: 4px;
  background: white url("@/static/images/arrow_right.svg") no-repeat 95% 50%;
  background-size: 12px;
  color: #0079bf;
  font-weight: 700;
  cursor: pointer;
}

.workspace:hover {
  background: rgba(150, 180, 231, 0.32) url("@/static/images/arrow_right.svg") no-repeat 95% 50%;
  background-size: 12px;
}

.add {
  cursor: pointer;
}

.add:hover {
  background: rgba(150, 180, 231, 0.32);
}

.open__menu-label {
  margin-top: 8px;
  border-radius: 4px;
  padding: 8px;
  padding-left: 28px;
  display: flex;
  align-items: center;
  color: #42526e;
  font-size: 12px;
  transition: background-color 64ms;
}

.open__menu-label:hover {
  background: rgba(150, 180, 231, 0.32);
}

.open__lbl {
  padding-left: 8px;
}


.new__wk-back {
  padding: 50px;
  width: 100%;
  height: 800px;
  background: rgba(128, 128, 128, 0.55);
  position: absolute;
  display: flex;
  justify-content: center;
}

.new__wk {
  background: linear-gradient(to right, white 50%, #d6ffec 50%);
  width: 90%;
  height: 700px;
  border-radius: 8px;
  display: flex;
}


</style>