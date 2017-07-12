package qa.learningapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class LoginActivity extends AppCompatActivity {

  @BindView(R.id.editText_username) EditText editText_username;
  @BindView(R.id.editText_password) EditText editText_password;
  @BindView(R.id.textView_forgot) TextView textView_forgot;
  @BindView(R.id.button_login) Button button_login;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_login);
    ButterKnife.bind(this);

  }

  @OnClick(R.id.button_login)
  public void onClickLogin() {
    if (!verify_login()) {
      return;
    }

    startActivity(new Intent(LoginActivity.this, MainActivity.class));
  }

  private boolean verify_login() {

    String username = editText_username.getText().toString().trim();
    String password = editText_password.getText().toString();

    if (!isValidEmail(username)) {
      DialogFactory.error_toast(LoginActivity.this, "invalid email").show();
      return false;
    }

    if (password.length() < 6) {
      DialogFactory.error_toast(LoginActivity.this, "password should be at least 6 characters").show();
      return false;
    }

    if(!username.equals("test@test.com") || !password.equals("123456")){
      DialogFactory.error_toast(LoginActivity.this, "invalid username or password"
          + "").show();
      return false;
    }

    return true;
  }

  @OnClick(R.id.textView_forgot)
  public void onClickForgot() {
    DialogFactory.error_toast(LoginActivity.this, "Ops! An Error Occurred").show();
  }

  private static boolean isValidEmail(CharSequence target) {
    return !TextUtils.isEmpty(target) && android.util.Patterns.EMAIL_ADDRESS.matcher(target).matches();
  }
}
