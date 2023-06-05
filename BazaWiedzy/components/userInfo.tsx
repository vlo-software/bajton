import type { UserData } from "@/hooks/useAuth";

export default function UserInfo({
  userData,
  loading,
}: {
  userData: UserData | null;
  loading: boolean;
}) {
  if (loading || userData === null)
    return (
      <>
        <div className="h-full flex flex-row justify-end items-center">
          <div className="animate-pulse mr-5">
            <div className="h-5 bg-slate-300 rounded-lg dark:bg-slate-600 w-48"></div>
          </div>
          <div className="h-full">
            <img
              alt="user avatar"
              className="h-full p-1 rounded-full mr-5 animate-pulse"
              src={"/public/avatar/default.png"}
            />
          </div>
        </div>
      </>
    );
  return (
    <>
      <div
        data-testid="userinfo-container"
        className="h-full flex flex-row justify-end items-center"
      >
        <div className="mr-5 text-lg">{userData.user.username}</div>
        <div className="h-full">
          <img
            alt="user avatar"
            className="h-full p-1 rounded-full mr-5"
            src={userData.avatar}
          />
        </div>
      </div>
    </>
  );
}
