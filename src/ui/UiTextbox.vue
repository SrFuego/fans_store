<template>
    <div class="ui-textbox" :class="classes">
        <div class="ui-textbox__icon-wrapper" v-if="icon || $slots.icon">
            <slot name="icon">
                <ui-icon :icon="icon"></ui-icon>
            </slot>
        </div>

        <div class="ui-textbox__content">
            <label class="ui-textbox__label">
                <div
                    class="ui-textbox__label-text"
                    :class="labelClasses"
                    v-if="label || $slots.default"
                >
                    <slot>{{ label }}</slot>
                </div>
                <div v-if="showpass" :class="{'active-color' : activeEye}" class="ui-textbox__visibility" @click="changedType()">
                  <i class="material-icons">visibility</i>
                </div>
                <input
                    class="ui-textbox__input"
                    ref="input"

                    :autocomplete="autocomplete ? autocomplete : null"
                    :disabled="disabled"
                    :max="maxValue"
                    :maxlength="enforceMaxlength ? maxlength : null"
                    :min="minValue"
                    :name="name"
                    :number="type === 'number' ? true : null"
                    :placeholder="hasFloatingLabel ? null : placeholder"
                    :readonly="readonly"
                    :required="required"
                    :step="stepValue"
                    :type="type"
                    :value="value"

                    @blur="onBlur"
                    @change="onChange"
                    @focus="onFocus"
                    @input="updateValue($event.target.value)"
                    @keydown.enter="onKeydownEnter"
                    @keydown="onKeydown"

                    v-autofocus="autofocus"
                    v-if="!multiLine"
                >
                <textarea
                    class="ui-textbox__textarea"
                    ref="textarea"

                    :autocomplete="autocomplete ? autocomplete : null"
                    :disabled="disabled"
                    :maxlength="enforceMaxlength ? maxlength : null"
                    :name="name"
                    :placeholder="hasFloatingLabel ? null : placeholder"
                    :readonly="readonly"
                    :required="required"
                    :rows="rows"
                    :value="value"

                    @blur="onBlur"
                    @change="onChange"
                    @focus="onFocus"
                    @input="updateValue($event.target.value)"
                    @keydown.enter="onKeydownEnter"
                    @keydown="onKeydown"

                    v-autofocus="autofocus"
                    v-else
                >{{ value }}</textarea>
            </label>

            <div class="ui-textbox__feedback" v-if="hasFeedback || maxlength">
                <div class="ui-textbox__feedback-text" v-if="showError">
                    <slot name="error">{{ error }}</slot>
                </div>

                <div class="ui-textbox__feedback-text" v-else-if="showHelp">
                    <slot name="help">{{ help }}</slot>
                </div>

                <div class="ui-textbox__counter" v-if="maxlength">
                    {{ value.length + '/' + maxlength }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import autofocus from './directives/autofocus'
  import UiIcon from './UiIcon.vue'

  import autosize from 'autosize'

  export default {
    name: 'ui-textbox',
    props: {
      name: String,
      placeholder: String,
      value: {
        type: [String, Number],
        required: true
      },
      icon: String,
      iconPosition: {
        type: String,
        default: 'left' // 'left' or 'right'
      },
      label: String,
      floatingLabel: {
        type: Boolean,
        default: false
      },
      type: {
        type: String,
        default: 'text' // all the possible HTML5 input types, except those that have a special UI
      },
      showpass: {
        type: Boolean,
        default: false
      },
      multiLine: {
        type: Boolean,
        default: false
      },
      rows: {
        type: Number,
        default: 2
      },
      autocomplete: String,
      autofocus: {
        type: Boolean,
        default: false
      },
      autosize: {
        type: Boolean,
        default: true
      },
      min: Number,
      max: Number,
      step: {
        type: String,
        default: 'any'
      },
      maxlength: Number,
      enforceMaxlength: {
        type: Boolean,
        default: false
      },
      required: {
        type: Boolean,
        default: false
      },
      readonly: {
        type: Boolean,
        default: false
      },
      help: String,
      error: String,
      invalid: {
        type: Boolean,
        default: false
      },
      disabled: {
        type: Boolean,
        default: false
      }
    },
    data () {
      return {
        activeEye: false,
        isActive: false,
        isTouched: false,
        initialValue: this.value,
        autosizeInitialized: false
      }
    },
    computed: {
      classes () {
        return [
          `ui-textbox--icon-position-${this.iconPosition}`,
          { 'is-active': this.isActive },
          { 'is-invalid': this.invalid },
          { 'is-touched': this.isTouched },
          { 'is-multi-line': this.multiLine },
          { 'has-counter': this.maxlength },
          { 'is-disabled': this.disabled },
          { 'has-label': this.hasLabel },
          { 'has-floating-label': this.hasFloatingLabel }
        ]
      },
      labelClasses () {
        return {
          'is-inline': this.hasFloatingLabel && this.isLabelInline,
          'is-floating': this.hasFloatingLabel && !this.isLabelInline
        }
      },

      hasLabel () {
        return Boolean(this.label) || Boolean(this.$slots.default)
      },

      hasFloatingLabel () {
        return this.hasLabel && this.floatingLabel
      },

      isLabelInline () {
        return this.value.length === 0 && !this.isActive
      },

      minValue () {
        if (this.type === 'number' && this.min !== undefined) {
          return this.min
        }
        return null
      },

      maxValue () {
        if (this.type === 'number' && this.max !== undefined) {
          return this.max
        }
        return null
      },

      stepValue () {
        return this.type === 'number' ? this.step : null
      },

      hasFeedback () {
        return Boolean(this.help) || Boolean(this.error) || Boolean(this.$slots.error)
      },

      showError () {
        return this.invalid && (Boolean(this.error) || Boolean(this.$slots.error))
      },

      showHelp () {
        return !this.showError && (Boolean(this.help) || Boolean(this.$slots.help))
      }
    },
    created () {
      // Normalize the value to an empty string if it's null
      if (this.value === null) {
        this.initialValue = ''
        this.updateValue('')
      }
    },
    mounted () {
      if (this.multiLine && this.autosize) {
        autosize(this.$refs.textarea)
        this.autosizeInitialized = true
      }
    },

    beforeDestroy () {
      if (this.autosizeInitialized) {
        autosize.destroy(this.$refs.textarea)
      }
    },

    methods: {
      updateValue (value) {
        this.$emit('input', value)
      },
      changedType () {
        if (this.showpass) {
          this.$nextTick(() => {
            this.activeEye = !this.activeEye
            this.type = this.type === 'text' ? 'password' : 'text'
          })
        }
      },

      onChange (e) {
        this.$emit('change', this.value, e)
      },

      onFocus (e) {
        this.isActive = true
        this.$emit('focus', e)
      },

      onBlur (e) {
        this.isActive = false
        this.$emit('blur', e)

        if (!this.isTouched) {
          this.isTouched = true
          this.$emit('touch')
        }
      },

      onKeydown (e) {
        this.$emit('keydown', e)
      },

      onKeydownEnter (e) {
        this.$emit('keydown-enter', e)
      },

      reset () {
        // Blur the input if it's focused to prevent required errors
        // when it's value is reset
        if (document.activeElement === this.$refs.input || document.activeElement === this.$refs.textarea) {
          document.activeElement.blur()
        }
        this.updateValue(this.initialValue)
        this.resetTouched()
      },

      resetTouched (options = { touched: false }) {
        this.isTouched = options.touched
      },

      refreshSize () {
        if (this.autosizeInitialized) {
          autosize.update(this.$refs.textarea)
        }
      }
    },
    components: {
      UiIcon
    },

    directives: {
      autofocus
    }
  }
</script>

<style lang="scss">
@import './styles/imports';

.ui-textbox {
  align-items: flex-start;
  display: flex;
  margin-bottom: $ui-input-margin-bottom;

  /*
  &:hover:not(.is-disabled) {
      .ui-textbox__label-text {
          color: $ui-input-label-color--hover;
      }

      .ui-textbox__input,
      .ui-textbox__textarea {
          border-bottom-color: $ui-input-border-color--hover;
      }
  }
  &.is-active:not(.is-disabled) {
      .ui-textbox__input,
      .ui-textbox__textarea {
          border-bottom-color: $ui-input-border-color--active;
          border-bottom-width: $ui-input-border-width--active;
      }

      .ui-textbox__label-text,
      .ui-textbox__icon-wrapper .ui-icon {
          color: $ui-input-label-color--active;
      }
  }
  */

  &.has-label {
      .ui-textbox__icon-wrapper {
          padding-top: $ui-input-icon-margin-top--with-label;
      }
  }

  &.has-counter {
      .ui-textbox__feedback-text {
          padding-right: rem-calc(48px);
      }
  }

  &.has-floating-label {
      .ui-textbox__label-text {
          // Behaves like a block, but width is the width of its content.
          // Needed here so label doesn't overflow parent when scaled.
          display: table;

          &.is-inline {
              color: $ui-input-label-color; // So the hover styles don't override it
              cursor: text;
              transform: translateY($ui-input-label-top--inline) scale(1.1);
          }

          &.is-floating {
              transform: translateY(0) scale(1);
          }
      }
  }

  &.is-invalid:not(.is-disabled) {
      .ui-textbox__label-text,
      .ui-textbox__icon-wrapper .ui-icon,
      .ui-textbox__counter {
          color: $ui-input-label-color--invalid;
      }

      .ui-textbox__input,
      .ui-textbox__textarea {
          // border-bottom-color: $ui-input-border-color--invalid;
      }

      .ui-textbox__feedback {
          color: $ui-input-feedback-color--invalid;
      }
  }

  &.is-disabled {
      .ui-textbox__input,
      .ui-textbox__textarea {
          // border-bottom-style: $ui-input-border-style--disabled;
          // border-bottom-width: $ui-input-border-width--active;
          color: rgba(155, 155, 155, 0.45);
      }

      .ui-textbox__icon-wrapper .ui-icon {
          opacity: $ui-input-icon-opacity--disabled;
      }

      .ui-textbox__feedback {
          opacity: $ui-input-feedback-opacity--disabled;
      }
  }
}

.ui-textbox__label {
    display: block;
    margin: 0;
    padding: 0;
    width: 100%;
    position: relative;
}
.ui-textbox__visibility{
  position: absolute;
  right: 0;
  height: 46px;
  width: 40px;
  text-align: center;
  padding-top: 10px;
  top: 0;
  &.active-color{
    color: #00A63B;
  }
  .material-icons{
    display: block;
    margin: 0 auto;
  }
}

.ui-textbox__icon-wrapper {
    flex-shrink: 0;
    margin-right: rem-calc(12px);
    padding-top: $ui-input-icon-margin-top;

    .ui-icon {
        color: $ui-input-icon-color;
    }
}

.ui-textbox__content {
    flex-grow: 1;
}

.ui-textbox__label-text {
    font-size: $ui-input-label-font-size;
    line-height: $ui-input-label-line-height;
    transform-origin: left;
    color: #9B9B9B;
    margin-bottom: 10px;
    transition: color 0.1s ease, transform 0.2s ease;
}

.ui-textbox__input,
.ui-textbox__textarea {
    background: none;
    cursor: auto;
    display: block;
    font-weight: normal;
    margin: 0;
    outline: none;
    transition: border 0.1s ease;
    width: 100%;
    min-height: 46px;
    padding: 6px 10px;
    font-size: 14px;
    color: #9B9B9B;
    border: 1px solid #424242;
    border-radius: 6px;
    background-color: #212121;
}

.ui-textbox__input {
    height: $ui-input-height;
}

.ui-textbox__textarea {
    overflow-x: hidden;
    overflow-y: auto;
    padding-bottom: rem-calc(6px);
    resize: vertical;
}

.ui-textbox__feedback {
    color: $ui-input-feedback-color;
    font-size: $ui-input-feedback-font-size;
    line-height: $ui-input-feedback-line-height;
    margin: 0;
    padding-top: $ui-input-feedback-padding-top;
    position: relative;
}

.ui-textbox__counter {
    position: absolute;
    right: 0;
    top: $ui-input-feedback-padding-top;
}

// ================================================
// Icon position
// ================================================

.ui-textbox--icon-position-right {
    .ui-textbox__icon-wrapper {
        margin-left: rem-calc(8px);
        margin-right: 0;
        order: 1;
    }
}
</style>
